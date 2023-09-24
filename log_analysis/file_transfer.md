# File Transfer (10)

## Description

Can you find the name of the file exfiltrated from the target host?

[ftp.pcap](ChallengeFiles/ftp.pcap)

We downloaded the .pcap file, and filtered by File Transfer Protocol (FTP). One of the requests was "RETR COME_GET_ME.txt", meaning the request retrieved a file known as "COME_GET_ME.txt".

## Flag
```
COME_GET_ME.txt
```