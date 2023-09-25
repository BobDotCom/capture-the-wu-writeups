# Web Login (20)
## Description
Can you find the login attempt? Password is the flag.

[web1.pcap](ChallengeFiles/web1.pcap)

## Solution

Immedately we put a display filter on for http requests. We could filter even more for a POST request, as information would have to be sent to log in and login requests are typically POST requests, but the request can already be seen. 

A POST request to /rest/user/login probably is the login request, checking the json data, we see email and password fields.
```
POST /rest/user/login HTTP/1.1
Host: 172.24.229.247:3000
Connection: keep-alive
Content-Length: 59
Accept: application/json, text/plain, */*
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76
Content-Type: application/json
Origin: http://172.24.229.247:3000
Referer: http://172.24.229.247:3000/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: language=en; cookieconsent_status=dismiss

{"email":"bender@juice-sh.op","password":"NOT_MY_PASSWORD"}

```
the password, NOT_MY_PASSWORD, is the flag.

## Flag
```
NOT_MY_PASSWORD
```