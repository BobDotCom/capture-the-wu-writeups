# File Transfer (10)

## Description

Can you find the name of the file exfiltrated from the target host?

[ftp.pcap](ChallengeFiles/ftp.pcap)


## Solution

Due to the challenge name "File Transfer" and the file name "ftp.pcap," the first thing we did is add a display filter for FTP requests (using Wireshark). After this, we are looking for requests that retrieve files. On packet number 3164, we see the command "RETR COME_GET_ME.txt". This command specifies retreiving (getting a copy of) the file "COME_GET_ME.txt". This is the action specified in the description, so we know that the name of this file is the flag.

## Flag
```
COME_GET_ME.txt
```