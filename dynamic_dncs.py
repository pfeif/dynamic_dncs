"""
Dynamic DNcS (Dynamic Domain Namecheap System)

A very simple Dynamic DNS record updater that works with your Namecheap domain.
"""

import sys
import tomllib
from pathlib import Path
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import urlopen

CONFIG_FILE = 'config.toml'


def main() -> None:
    """Update the Dynamic DNS records for each entry in the config file."""
    try:
        working_dir = Path(__file__).parent
        config_path = working_dir / CONFIG_FILE

        with config_path.open('rb') as config_file:
            config = tomllib.load(config_file)

        hosts = config['hosts']

        current_ip = ''
        ip_lookup_required = any(not host.get('ip') for host in hosts)

        if ip_lookup_required:
            current_ip = get_ip_address()

        for host in hosts:
            host_name = host.get('host', '')
            domain = host.get('domain', '')
            ip_addr = host.get('ip', '')
            password = host.get('password', '')

            if ip_addr:
                pass
            elif current_ip:
                ip_addr = current_ip
            else:
                print('Skipping host. Unable to determine current IP address.')
                continue

            if not all([host_name, domain, password]):
                print('Skipping host. Missing required field')
                continue

            update_record(host_name, domain, password, ip_addr)
    except Exception as e:
        print(f'An unknown error occurred: {e}')
        sys.exit(1)


def get_ip_address() -> str:
    """Return a string with the current external IP address."""
    try:
        with urlopen('https://dynamicdns.park-your-domain.com/getip', timeout=15) as response:
            current_ip = response.read().decode().strip()
            return current_ip
    except URLError as e:
        raise ConnectionError(f'Error: Unable to get current IP address: {e.reason}') from e


def update_record(host: str, domain: str, password: str, ip_addr: str) -> None:
    """Update the DNS record to the given IP address."""
    base_url = 'https://dynamicdns.park-your-domain.com/update'
    query_string = urlencode({'host': host, 'domain': domain, 'password': password, 'ip': ip_addr})

    try:
        with urlopen(f'{base_url}?{query_string}', timeout=15):
            pass
    except URLError as e:
        raise ConnectionError(f'Error: Unable to update DNS record for host {host}.{domain}: {e.reason}') from e


if __name__ == '__main__':
    main()
