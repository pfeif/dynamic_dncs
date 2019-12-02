# Dynamic DNcS (Dynamic Domain Namecheap System)
TL;DR: Edit `HOST`, `DOMAIN`, and `PASSWORD` at the top of ddncs.py to
configure. Run manually at command line with `python3 ddncs.py` or set up a
scheduler like cron.

Dynamic DNcS (or DDNcS) is a very simple Dynamic DNS record updater that works
with your Namecheap domain. Many people have written "lite" address-updating
programs which either employ a web UI or include a helpful command line menu or
work with 20 different services. This isn't any of those. DDNcS is just a
simple Python 3 script that does the bare minimum to update your DNS record
with Namecheap.

I wrote DDNcS years ago out of frustration with setting up
[ddclient](https://github.com/ddclient/ddclient). I appreciate the hard work
that must go into maintaining a 5000+ line Perl script, but getting ddclient
set up and playing nicely with systemd has always been just out of reach for
me. This is a woe that I recently relived when I performed a fresh OS install
on my always-on Raspberry Pi server. Shortly after manually installing the
latest version of ddclient (which now supposedly
[supports https](https://github.com/ddclient/ddclient/blob/master/ChangeLog)
with Namecheap), installing all of the Perl dependencies, and running into
nothing but trouble with systemd and PID files, I remembered this little
bit of code from long ago.

I plan to update DDNcS soon with a dead-simple IP address cache system and the
ability to pass a host/IP combo at the command line, but that's it! That's
where it stops.

Until that's done, you can configure the program by editing the global `HOST`,
`DOMAIN`, and `PASSWORD` variables at the top of ddncs.py. You can either run
the program manually by calling `python3 ddncs.py` at the command line or
setting up a cron job by running `crontab -e` and scheduling as you see fit.
[crontab.guru](https://crontab.guru/) might be able to help you with that, but
I think `@reboot` is a good option. (I don't know crontab guru. I just like the
website.)
