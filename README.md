# Dynamic DNcS (Dynamic Domain Namecheap System)

## TL;DR

Replace example settings in [settings.json][settings] with your own. Run
manually at command line with `python dynamic_dncs.py` or set up a task
scheduler to automate the process.

## About

Dynamic DNcS, or DDNcS, is a very simple Dynamic DNS record updater that works
with your Namecheap domain. Many people have written "lite" address-updating
programs which either employ a web UI or include a helpful command line menu or
work with 20 different services. This isn't any of those. DDNcS is just a
simple [Python][python] script that does the bare minimum to update your DNS
record with Namecheap.

I wrote DDNcS years ago out of frustration with setting up
[DDclient][ddclient]. I appreciate the hard work that must go into maintaining
5000+ lines of Perl, but getting DDclient set up and playing nicely with
systemd has always been just out of reach for me. This is a woe that I recently
relived when I performed a fresh OS install on my always-on Raspberry Pi
server. Shortly after manually installing the latest version of DDclient,
installing all of the Perl dependencies, and running into nothing but trouble
with systemd and PID files, I remembered this little bit of code from long ago.

I'm considering updating DDNcS with a simple IP address cache system and the
ability to pass a host/IP combo at the command line, but that's it! That's
where it'll stop.

## Prerequisites

 * [A recent version of Python][python-downloads]

## Usage

You can configure the program settings by editing your
[settings.json][settings] file. Example settings are provided in the file and
should be replaced with your own. The password is *not* your Namecheap account
password. It is the Dynamic DNS password which can be found under the "Advanced
DNS" section when you click on the "Manage" button next to your domain. A
simple settings.json might look like this:

```JSON
{
    "hosts": [
        {
            "host": "@",
            "domain": "example.com",
            "ip": "",
            "password": "32CharacterAlphaNumericPassword1"
        }
    ]
}
```

You can either run the program manually by executing
`python dynamic_dncs.py` at the command line or by setting up a cron job (by
running `crontab -e`) and scheduling as you see fit. [crontab.guru][crontab]
might be able to help you with that. My current crontab file looks like this:

```
# Update DNS on every reboot
@reboot sleep 60; python /path/to/dynamic_dncs.py

# Update DNS every day at 7:00 AM
0 7 * * * python /path/to/dynamic_dncs.py

```

## License

This project is licensed under the terms of the MIT license. See
[LICENSE.md][license] for details.

[crontab]: https://crontab.guru/
[ddclient]: https://ddclient.net/
[license]: LICENSE.md
[python-downloads]: https://www.python.org/downloads/
[python]: https://www.python.org/
[settings]: settings.json
