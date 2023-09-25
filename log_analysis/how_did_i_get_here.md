# How Did I Get Here (10)

## Description

A new user has been created. Can you find the username?

[user.evtx](ChallengeFiles/user.evtx)

## Solution

Manually looking through all events, the event at 9:44:52am with EventID 4720 says the following:
```
A user account was created.

Subject:
	Security ID:		S-1-5-21-3214064836-1759666845-3650452130-1002
	Account Name:		steve
	Account Domain:		WIN-10-VIC
	Logon ID:		0x102B52

New Account:
	Security ID:		S-1-5-21-3214064836-1759666845-3650452130-1008
	Account Name:		SUPER_STEVE_ADMIN
	Account Domain:		WIN-10-VIC

Attributes:
	SAM Account Name:	SUPER_STEVE_ADMIN
	Display Name:		<value not set>
	User Principal Name:	-
	Home Directory:		<value not set>
...
```

Here we see a user account being created with the name SUPER_STEVE_ADMIN, this is the flag.

## Flag

```
SUPER_STEVE_ADMIN
```