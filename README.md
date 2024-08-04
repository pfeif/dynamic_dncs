# Dynamic DNcS (Dynamic Domain Namecheap System)

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

## Settings

You can configure the program settings by editing the [settings.json][settings]
file. Example settings are provided in the file and should be replaced with
your own. The password is *not* your Namecheap account password. It is the
Dynamic DNS password which can be found under the "Advanced DNS" section when
you click on the "Manage" button next to your domain. A simple settings.json
might look like this:

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

## Executing

### Python

The first option for running this script is using your local Python
installation. The only thing you need is a currently-supported version of
Python.

The script uses only built-in Python libraries, so there's nothing to pip
install, no virtual environments to create or maintain, and no potential for
typo squatting vulnerabilities on PyPI.

It's as simple as updating `settings.json` and running `python dynamic_dncs.py`
in the command line.

### Docker

If you can't or don't want to install Python, but you do have access to Docker,
you can use the included Docker configuration files to set up and run the
containers.

#### Download and create the required Docker assets

```Shell
docker compose up --detach
```

#### Execute the script

```Shell
docker start dynamic_dncs
```

#### Remove the created Docker assets

Note: This does not remove the python:slim image downloaded during setup.

```Shell
docker compose down
```

### Task Scheduler

It's convenient for me to run DDNcS with a task scheduler. You can use cron,
systemd, or just about any other task manager you like.

I prefer to use cron, and I prefer to execute the script once a day and every
time my Raspberry Pi restarts. The idea is that if the power goes out, it's
likely that my dynamic IP will change and the dynamic DNS address will need to
be updated with Namecheap.

To edit your cron configuration file, execute `crontab -e` in the command line.
[crontab.guru][crontab] might be helpful with finding the right configuration
for you, but my crontab file might look something like this:

#### Using local Python installation

```
# Update DNS on every reboot
@reboot sleep 60; python /path/to/dynamic_dncs.py

# Update DNS every day at 7:00 AM
0 7 * * * python /path/to/dynamic_dncs.py
```

#### Using Docker container

```
# Update DNS on every reboot
@reboot sleep 60; docker start dynamic_dncs

# Update DNS every day at 7:00 AM
0 7 * * * docker start dynamic_dncs
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
