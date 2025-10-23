# Dynamic DNcS (Dynamic Domain Namecheap System)

## About

Dynamic DNcS, or DDNcS, is a very simple Dynamic DNS record updater that works
with your Namecheap domains. It's a one-file Python script that does the bare
minimum to update your Namecheap DNS records.

## Configuration

You can set the domain configurations by editing the [config.toml][config]
file. Examples are provided in the file and should be replaced with your own.
You may add as many as you'd like. If you have one domain to update, one is all
you need. If you have 50 domains to update, add all 50.

A minimal `config.toml` to update my-dns.example.com to your current IP might
look like this:

```toml
[[hosts]]
host = "my-dns"
domain = "example.com"
ip = ""
password = "32CharacterAlphaNumericPassword1"
```

*Note*: The password field is not for your Namecheap account password. It is the
Dynamic DNS password which can be found under the "Advanced DNS" section when
you click on the "Manage" button next to your domain.

## Executing

### Python

The first option for running this script is using your local Python
installation. The only thing you need is Python version 3.11 or newer. The
script uses only built-in Python libraries, so there's nothing to pip install,
no virtual environments to create or maintain, and no potential for typo
squatting vulnerabilities on PyPI.

It's as simple as updating `config.toml` and running `python dynamic_dncs.py`
in the command line. Of course, you're also free to run using tools like [uv][]
if you'd prefer.

### Docker

If you can't or don't want to install Python, but you do have access to Docker,
you can use the included Docker configuration files to set up and run the
containers.

#### Initial execution

The following command will:

- download the [`python:slim`][python-image] image from Docker to your machine
- create a Docker container named `dynamic_dncs`
- copy the contents of you current directory into the container
- run the container, executing the Python script

```shell
docker compose up --detach
```

#### Subsequent executions

The following command will re-run the existing `dynamic_dncs` container.

```shell
docker start dynamic_dncs
```

#### Cleaning up

The following will remove the `dynamic_dncs` container and all of its data from
your machine. It will not, however, remove the Docker image.

```shell
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
[crontab.guru][crontab] and my [cron template][cron-template] might be helpful
with finding the right configuration for you, but my crontab file probably looks
something like this right now:

#### Using local Python installation

```crontab
# Update DNS on every reboot
@reboot sleep 60; python /path/to/dynamic_dncs.py

# Update DNS every day at 7:00 AM
0 7 * * * python /path/to/dynamic_dncs.py
```

#### Using Docker container

```crontab
# Update DNS on every reboot
@reboot sleep 60; docker start dynamic_dncs

# Update DNS every day at 7:00 AM
0 7 * * * docker start dynamic_dncs
```

## License

This code is licensed under the very permissive, open-source BSD-3 Clause
license. Details can be found in [`LICENSE.md`](./LICENSE.md).

The TL;DR of the license is that you can do whatever you want with the extension
so long as you don't claim I endorse it.

[config]: config.toml
[cron-template]: https://gist.github.com/pfeif/5f49d6d3dde83ba82004552f784ed2ad
[crontab]: https://crontab.guru/
[python-image]: https://hub.docker.com/_/python
[uv]: https://docs.astral.sh/uv/
