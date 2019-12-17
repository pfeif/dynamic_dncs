"""
Dynamic DNcS (Dynamic Domain Namecheap System)

A very simple Dynamic DNS record updater that works with your Namecheap domain.
"""

import json             # to parse user-defined settings
import urllib.request   # to open URLs for getting/setting IP address

# The JSON file that holds the Namecheap host settings is assumed to be named
# settings.json and is expected to be in the same path as this program.
SETTINGS_FILE = "my_settings.json"


def main():
    # Open the settings file for reading and save it as a dictionary.
    with open(SETTINGS_FILE, "r") as settings_file:
        settings_dict = json.load(settings_file)

    # Process each host in the dictionary.
    for host in settings_dict["hosts"]:
        # If the user did not set an IP manually, use the current external IP.
        if not host["ip"]:
            host["ip"] = check_ip()

        # Update the DNS for the host.
        update_host(host["host"], host["domain"], host["password"], host["ip"])


def check_ip():
    """ Return a string of the current external IP address."""
    # Get the computer's external IP address from Namecheap
    response = urllib.request.urlopen(
        "https://dynamicdns.park-your-domain.com/getip")

    # response is an HTTPResponse object. Read its contents.
    ip_bytes = response.read()

    # The contents were bytes. Decode to a string.
    ip_str = ip_bytes.decode()

    # Return the result.
    return ip_str


def update_host(host, domain, password, ip_addr):
    """ Update the DDNS record to the given IP address. """
    # Create the URL string that will update the DNS with Namecheap.
    update_addr = "https://dynamicdns.park-your-domain.com/update?"\
                  "host={0}&domain={1}&password={2}&ip={3}".format(
                  host, domain, password, ip_addr)

    # Open the URL to complete the update.
    urllib.request.urlopen(update_addr)


if __name__ == "__main__":
    main()
