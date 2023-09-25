# We Need More Power (20)

## Description
Can you find the privilege escalation to the system user?

[priv.evtx](ChallengeFiles/priv.evtx)

## Solution

Starting this challenge, I was unfamilliar with windows events so when I opened the file, I looked at the first few events. The first fiew events with Id 4798 showed many users including: steve, SuperSteve, and SUPER_STEVE_ADMIN. These looked like they could be useful as they look like accounts with increasing levels of priveledge.

I searched for SUPER_STEVE_ADMIN as that seemed like the most interesting user, and the one with the hightest priveledge, but I didnt find anything noticeable, just a few events of the user logging in.

I then manually combed through the events and found something that I believed looked like priveledge escalation. At 10:04:59am, there were three Logon events:
1.
```
A logon was attempted using explicit credentials.

Subject:
	Security ID:		SYSTEM
	Account Name:		WIN-10-VIC$
	Account Domain:		WORKGROUP
	Logon ID:		0x3E7
	Logon GUID:		{00000000-0000-0000-0000-000000000000}

Account Whose Credentials Were Used:
	Account Name:		steve
	Account Domain:		WIN-10-VIC
	Logon GUID:		{00000000-0000-0000-0000-000000000000}
```
2.
```
Subject:
	Security ID:		SYSTEM
	Account Name:		WIN-10-VIC$
	Account Domain:		WORKGROUP
	Logon ID:		0x3E7

Logon Information:
	Logon Type:		10
	Restricted Admin Mode:	No
	Virtual Account:		No
	Elevated Token:		Yes

Impersonation Level:		Impersonation
```
3.
```
Subject:
	Security ID:		SYSTEM
	Account Name:		WIN-10-VIC$
	Account Domain:		WORKGROUP
	Logon ID:		0x3E7

Logon Information:
	Logon Type:		10
	Restricted Admin Mode:	No
	Virtual Account:		No
	Elevated Token:		No

Impersonation Level:		Impersonation
```

These events to me seemed like they could be priveledge escalation. In the first event, someone logging into SYSTEM with the credentials of steve seems like steve is gaining access to the SYSTEM account. The following Logon events were of user SYSTEM and also included things such as "Elevated Token" and "Impersionaltion Level: Impersionation" which seemed to support my conclusion. However, there was no obvious flag here. Nothing here was specicial or out of the ordinary to where it could be used as a flag. For this reason, I kept looking.

I eventually came across An event at 10:06:28am with eID of 4698. This event shows a scheduled task with the name of RIGHT_ON_SCHEDULE being created. Because of the name, this already stands out as that name is not a normal windows task. Looking into the task more, we see the following:

```xml
<Actions Context="Author">
    <Exec>
        <Command>cmd.exe</Command>
    </Exec>
</Actions>
<Principals>
    <Principal id="Author">
        <UserId>S-1-5-18</UserId>
        <RunLevel>LeastPrivilege</RunLevel>
    </Principal>
</Principals>
```

Here we see that this scheduled task opens the command prompt with the user "S-1-5-18." Looking into other events, we see that that userId is the id of SYSTEM. Ex.

```
Subject :
	Security ID:		SYSTEM
	Account Name:		WIN-10-VIC$
	Account Domain:		WORKGROUP
	Logon ID:		0x3E7
...
<Data Name="SubjectUserSid">S-1-5-18</Data> 
```

Because of this, we can conclude that this scheduled task runs cmd.exe as SYSTEM, this would give elevated priveledges. 
The only part about this event that stands out is the name, RIGHT_ON_SCHEDULE. We submitted this as the flag and it was correct.

### Flag
```
RIGHT_ON_SCHEDULE
```