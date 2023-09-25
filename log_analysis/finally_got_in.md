# Finally Got In (20)

## Description
Can you find the successful login attempt? Password is flag.

[web2.pcap](ChallengeFiles/web2.pcap)

## Solution

Put on a display filter for HTTP requests. This time we see multiple POST requests to /rest/user/login except all but the first one returns 401 unauthorized with the message "Invalid email or password." 

The second one sends a single quotation as the email and gets a 500 Internal server error response. We know that the sender is attempting some type of injection. 

The final one returns 200 OK and has a successful SQL injection for the email and a password of NO_PASS_NEEDED. This ended up being the flag, but we ended up going further and cracked the JWT sent back in the member token, "admin123" ended up being the jwt secret.

## Flag

```
NO_PASS_NEEDED
```
