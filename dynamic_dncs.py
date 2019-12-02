"""
Dynamic DNcS (Dynamic Domain Namecheap System)

A very simple Dynamic DNS record updater that works with your Namecheap domain.
"""

import urllib.request

# Replace these strings with your personalized settings.
HOST = '@'
DOMAIN = 'example.com'
PASSWORD = 's1cau4xdjtk2qfz0uop29l17m486c904'


def check_ip():
    """ Return a string of the current external IP address."""
    # Get the computer's external IP address from Namecheap
    req = urllib.request.urlopen(
          'https://dynamicdns.park-your-domain.com/getip')

    # req is an HTMLResponse object. Read its contents.
    ip_bytes = req.read()

    # The contents were bytes. Decode to a string.
    ip_str = ip_bytes.decode()

    # Return the result.
    return ip_str


def update_host(ip_addr):
    """ Update the DDNS record to the given IP address. """
    # Create the URL string that will update the DNS with Namecheap.
    update_addr = 'https://dynamicdns.park-your-domain.com/update?'\
                  'host={0}&domain={1}&password={2}&ip={3}'.format(
                   HOST, DOMAIN, PASSWORD, ip_addr)

    # Open the URL to complete the update.
    urllib.request.urlopen(update_addr)


def main():
    # Update the DNS record using the current external IP.
    update_host(check_ip())


if __name__ == '__main__':
    main()
