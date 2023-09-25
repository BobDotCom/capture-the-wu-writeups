# SMB Connections? (30) 
## Description
There was an SMB connection, can you find users password?

[smb.pcap](ChallengeFiles/smb.pcap)

## Solution

We filtered for smb2 and looked through the requests, but didnt find much. We researched and found out that the password hash is stored in the ntlm data. We found a script to parse and put together the NTLMv2 hash here: https://github.com/mlgualtieri/NTLMRawUnHide/

We ran it and found the hash to be

```
steve::WORKGROUP:0d48bf695527a1f7:b6c2448f56d24bb16e33ac8ff4be5bb1:010100000000000018a3dc75d8e0d9014e9f4da2df26f08f0000000002001c00570045002d0047004f0054002d005300430041004e004e004500440001001c00570045002d0047004f0054002d005300430041004e004e004500440004001c00570045002d0047004f0054002d005300430041004e004e004500440003001c00570045002d0047004f0054002d005300430041004e004e00450044000700080018a3dc75d8e0d9010600040002000000080030003000000000000000000000000000000077a0de6206725866ed136c31ddbba01e25e281fb92f35ea027aba3ec3e51c8c90a001000000000000000000000000000000000000900220063006900660073002f003100390032002e003100360038002e0030002e003500300000000000
```

I then put this into a file and ran john on the file with the wordlist given. John auto detected the format and found the password and the flag of SECRET_PASSWORD_DON'T_LOOK

## Flag
```
SECRET_PASSWORD_DON'T_LOOK
```