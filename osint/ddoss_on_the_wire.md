# DDosS on the Wire (20)

## Description
You have been tasked to recon the Wired.com site. One of your specific bits of information you were told to find was the cache tool the website uses so you can explore a DDOS attack. Can you tell us what it is?

## Solution

We ran the following command to scan wired and hopefully list the services running:
```zsh
nmap -A -sV wired.com
```
-A: Enable OS detection, version detection, script scanning, and traceroute
-sV: Probe open ports to determine service/version info

Part of the output:

```
PORT    STATE SERVICE   VERSION
80/tcp  open  http      Varnish
```

Upon research, we see that Varnish is a Cache tool: https://varnish-cache.org/, this is our flag

## Flag

```
CTFWU{Varnish}
```