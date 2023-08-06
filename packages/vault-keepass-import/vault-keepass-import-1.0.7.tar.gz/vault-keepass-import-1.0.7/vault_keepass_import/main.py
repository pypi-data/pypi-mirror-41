#!/usr/bin/env python
# coding: utf-8


from __future__ import print_function
from __future__ import unicode_literals
import argparse
import base64
import getpass
import hvac
from pykeepass import PyKeePass
import logging
import os
import re


logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)


def get_path(vault_backend, entry):
    path = entry.parentgroup.path
    if path[0] == '/':
        return vault_backend + '/' + entry.title
    else:
        return vault_backend + '/' + path + '/' + entry.title


def export_entries(filename, password, keyfile=None, skip_root=False):
    all_entries = []
    kp = PyKeePass(filename, password=password, keyfile=keyfile)
    for entry in kp.entries:
        if skip_root and entry.parentgroup.path == '/':
            continue
        all_entries.append(entry)
    logger.info('Total entries: {}'.format(len(all_entries)))
    return all_entries


def reset_vault_secrets_engine(url, token, path, cert, verify):
    client = hvac.Client(
        url=url, token=token, cert=cert, verify=verify
    )
    try:
        client.sys.disable_secrets_engine(path=path)
    except hvac.exceptions.InvalidRequest as e:
        if e.message == 'no matching mount':
            logging.error('Could not delete backend: Mount point not found.')
        else:
            raise
    client.sys.enable_secrets_engine(backend_type='kv', options={'version': '2'}, path=path)


def get_next_similar_entry_index(vault_url, vault_token, entry_name, cert, verify):
    client = hvac.Client(url=vault_url, token=vault_token, cert=cert, verify=verify)
    index = 0
    try:
        title = os.path.basename(entry_name)
        children = client.secrets.kv.v2.list_secrets(os.path.dirname(entry_name))
        for child in children['data']['keys']:
            m = re.match(title + r' \((\d+)\)$', child)
            if m:
                index = max(index, int(m.group(1)))
    except hvac.exceptions.InvalidPath:
        pass
    except Exception:
        raise
    return index + 1


def generate_entry_path(vault_url, vault_token, entry_path, cert, verify):
    next_entry_index = get_next_similar_entry_index(
        vault_url, vault_token, entry_path, cert, verify
    )
    new_entry_path = '{} ({})'.format(entry_path, next_entry_index)
    logger.info(
        'Entry "{}" already exists, '
        'creating a new one: "{}"'.format(entry_path, new_entry_path)
    )
    return new_entry_path


def keepass_entry_to_dict(e):
    entry = {}
    for k in ('username', 'password', 'url', 'notes', 'tags', 'icon', 'uuid'):
        if getattr(e, k):
            entry[k] = getattr(e, k)
    custom_properties = e.custom_properties
    # remove this workaround when https://github.com/pschmitt/pykeepass/pull/138 is merged
    if 'Notes' in custom_properties:
        del custom_properties['Notes']
    entry.update(custom_properties)
    if e.expires:
        entry['expiry_time'] = str(e.expiry_time.timestamp())
    for k in ('ctime', 'atime', 'mtime'):
        if getattr(e, k):
            entry[k] = str(getattr(e, k).timestamp())
    if hasattr(e, 'attachments'):  # implemented in pykeepass >= 3.0.3
        for a in e.attachments:
            entry[f'{a.id}/{a.filename}'] = base64.b64encode(a.data).decode('ascii')
    return entry


def vault_entry_to_dict(e):
    return e['data']['data']


def export_to_vault(keepass_db, keepass_password, keepass_keyfile,
                    vault_url, vault_token, vault_backend, cert, verify,
                    force_lowercase=False, skip_root=False, allow_duplicates=True):
    entries = export_entries(
        keepass_db, keepass_password, keepass_keyfile,
        skip_root
    )
    client = hvac.Client(
        url=vault_url, token=vault_token, cert=cert, verify=verify
    )
    r = {}
    for e in entries:
        entry = keepass_entry_to_dict(e)
        entry_path = get_path(vault_backend, e)
        if force_lowercase:
            entry_path = entry_path.lower()
        try:
            exists = client.secrets.kv.v2.read_secret_version(entry_path)
        except hvac.exceptions.InvalidPath:
            exists = None
        except Exception:
            raise
        if allow_duplicates:
            if exists:
                entry_path = generate_entry_path(
                    vault_url, vault_token, entry_path, cert, verify)
            r[entry_path] = 'changed'
        else:
            if exists:
                r[entry_path] = entry == vault_entry_to_dict(exists) and 'ok' or 'changed'
            else:
                r[entry_path] = 'changed'
        logger.info(f'{r[entry_path]}: {entry_path} => {entry}')
        if r[entry_path] == 'changed':
            client.secrets.kv.v2.create_or_update_secret(entry_path, entry)
    return r


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--verbose',
        action='store_true',
        required=False,
        help='Verbose mode'
    )
    parser.add_argument(
        '-p', '--password',
        required=False,
        help='Password to unlock the KeePass database'
    )
    parser.add_argument(
        '-f', '--keyfile',
        required=False,
        help='Keyfile to unlock the KeePass database'
    )
    parser.add_argument(
        '-t', '--token',
        required=False,
        default=os.getenv('VAULT_TOKEN', None),
        help='Vault token'
    )
    parser.add_argument(
        '-v', '--vault',
        default=os.getenv('VAULT_ADDR', 'https://localhost:8200'),
        required=False,
        help='Vault URL'
    )
    parser.add_argument(
        '-k', '--ssl-no-verify',
        action='store_true',
        default=True if os.getenv('VAULT_SKIP_VERIFY', False) else False,
        required=False,
        help='Whether to skip TLS cert verification'
    )
    parser.add_argument(
        '-s', '--skip-root',
        action='store_true',
        required=False,
        help='Skip KeePass root folder (shorter paths)'
    )
    parser.add_argument(
        '--ca-cert',
        required=False,
        help=("Path on the local disk to a single PEM-encoded CA certificate to verify "
              "the Vault server's SSL certificate.")
    )
    parser.add_argument(
        '--client-cert',
        required=False,
        help='client cert file'
    )
    parser.add_argument(
        '--client-key',
        required=False,
        help='client key file'
    )
    parser.add_argument(
        '--idempotent',
        action='store_true',
        required=False,
        help='An entry is overriden if it already exists, unless it is up to date'
    )
    parser.add_argument(
        '-b', '--backend',
        default='keepass',
        help='Vault backend (destination of the import)'
    )
    parser.add_argument(
        '--path',
        default='secret',
        help='KV mount point',
    )
    parser.add_argument(
        '-e', '--erase',
        action='store_true',
        help='Erase the prefix prior to the import operation'
    )
    parser.add_argument(
        '-l', '--lowercase',
        action='store_true',
        help='Force keys to be lowercased'
    )
    parser.add_argument(
        'KDBX',
        help='Path to the KeePass database'
    )
    args = parser.parse_args()

    password = args.password if args.password else getpass.getpass()
    if args.token:
        # If provided argument is a file read from it
        if os.path.isfile(args.token):
            with open(args.token, 'r') as f:
                token = filter(None, f.read().splitlines())[0]
        else:
            token = args.token
    else:
        token = getpass.getpass('Vault token: ')

    if args.verbose:
        level = logging.DEBUG
    else:
        level = logging.INFO
    logging.getLogger('vault_keepass_import').setLevel(level)

    if args.ssl_no_verify:
        verify = False
    else:
        if args.ca_cert:
            verify = args.ca_cert
        else:
            verify = True

    if args.erase:
        reset_vault_secrets_engine(
            url=args.vault,
            token=token,
            path=args.path,
            cert=(args.client_cert, args.client_key),
            verify=verify,
        )
    export_to_vault(
        keepass_db=args.KDBX,
        keepass_password=password,
        keepass_keyfile=args.keyfile,
        vault_url=args.vault,
        vault_token=token,
        vault_backend=args.backend,
        cert=(args.client_cert, args.client_key),
        verify=verify,
        force_lowercase=args.lowercase,
        skip_root=args.skip_root,
        allow_duplicates=not args.idempotent
    )
