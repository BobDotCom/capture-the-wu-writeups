# Who Nmaped me? (10)

## Description
Can you find the host name of the nmap target?

[nmap.pcap](ChallengeFiles/nmap.pcap)

## Solution

We see lots of tcp requests on random ports from 192.168.0.100 to 192.168.0.50 which looks like a nmap scan as it would scan and send request to many ports. At the end of the logs though, we see a broadcast from 192.168.0.50 that has a hostname of WE-GOT-SCANNED. Because the target was 192.168.0.50 and that ip's hostname is WE-GOT-SCANNED, that is the flag

## Flag
```
WE-GOT-SCANNED
```