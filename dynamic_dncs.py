"""
Dynamic DNcS (Dynamic Domain Namecheap System)

A very simple Dynamic DNS record updater that works with your Namecheap domain.
"""

import json
import urllib.request
from os import path

SETTINGS_FILE = "settings.json"


def main():
    """ Update the Dynamic DNS records for each entry in the settings file. """
    working_dir = path.dirname(__file__)
    with open(path.join(working_dir, SETTINGS_FILE), "r") as settings_file:
        settings = json.load(settings_file)

    for host in settings["hosts"]:
        if not host["ip"]:
            host["ip"] = check_ip()

        update_host(host["host"], host["domain"], host["password"], host["ip"])


def check_ip():
    """ Return a string of the current external IP address. """
    response = urllib.request.urlopen(
        "https://dynamicdns.park-your-domain.com/getip")

    current_ip = response.read().decode()

    return current_ip


def update_host(host, domain, password, ip_addr):
    """ Update the Dynamic DNS record to the given IP address. """
    update_addr = f"https://dynamicdns.park-your-domain.com/update?" \
        f"host={host}&domain={domain}&password={password}&ip={ip_addr}"

    urllib.request.urlopen(update_addr)


if __name__ == "__main__":
    main()
