# Dynamic DNcS (Dynamic Domain Namecheap System)

## TL;DR

Replace example settings in [settings.json](settings.json) with your own. Run
manually at command line with `python dynamic_dncs.py` or set up a task
scheduler like cron.

## About

Dynamic DNcS, or DDNcS, is a very simple Dynamic DNS record updater that works
with your Namecheap domain. Many people have written "lite" address-updating
programs which either employ a web UI or include a helpful command line menu or
work with 20 different services. This isn't any of those. DDNcS is just a
simple [Python 3](https://www.python.org/) script that does the bare minimum to
update your DNS record with Namecheap.

I wrote DDNcS years ago out of frustration with setting up
[ddclient](https://github.com/ddclient/ddclient). I appreciate the hard work
that must go into maintaining 5000+ lines of Perl, but getting ddclient set up
and playing nicely with systemd has always been just out of reach for me. This
is a woe that I recently relived when I performed a fresh OS install on my
always-on Raspberry Pi server. Shortly after manually installing the latest
version of ddclient (which now supposedly
[supports https](https://github.com/ddclient/ddclient/blob/master/ChangeLog)
with Namecheap), installing all of the Perl dependencies, and running into
nothing but trouble with systemd and PID files, I remembered this little
bit of code from long ago.

I'm considering updating DDNcS with a simple IP address cache system and the
ability to pass a host/IP combo at the command line, but that's it! That's
where it'll stop.

## Prerequisites

 * [Python 3.5 (or later)](https://www.python.org/downloads/)

## Usage

You can configure the program settings by editing
[settings.json](settings.json). Example settings are provided in the file and
should be replaced with your own. A simple settings.json might look like this:

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

You can either run the program manually by calling
`python dynamic_dncs.py` at the command line or by setting up a cron job (by
running `crontab -e`) and scheduling as you see fit.
[crontab.guru](https://crontab.guru/) might be able to help you with that, but
I think `@reboot sleep 60; python3 /path/to/dynamic_dncs.py` is a good option.
(Also, I don't know crontab guru. I just like the website.)

## License

This project is licensed under the terms of the MIT license. See
[LICENSE.md](LICENSE.md) for details.
