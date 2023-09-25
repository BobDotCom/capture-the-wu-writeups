# IoTeaser (20)

## Description
My networked refrigerator is spitting out Spam and it is making me sick watching it. Find the “current weakness” flag and we may solve the problem

## Solution
- We found an article on Proofpoint from 2014 about fridges that got hacked and sent hundreds of thousands of spam emails. This seemed fitting, as the challenge flag started with "IoT", which the article mentioned frequently. https://www.proofpoint.com/us/threat-insight/post/Your-Fridge-is-Full-of-SPAM
- We saw in the article that the issue was the fridges used default passwords/credentials.
- We found these possibilities
  - CWE-1393: Use of Default Password
  - CWE-1392: Use of Default Credentials
- Neither of them worked
