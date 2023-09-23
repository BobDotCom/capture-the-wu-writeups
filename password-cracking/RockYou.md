# Rock You - 10 Points
## Description
Question: You are conducting a security audit on a system and have obtained a list of password hashes from the database. You suspect that the passwords are weak and correspond to some passwords from the rockyou data breach. Can you decrypt the hashes?

## Solution
To crack these passwords, I used the tool "John the Ripper," which is a popular Open Source password-cracking tool. It can be installed using apt-get or snap on Linux, and through this link: https://www.openwall.com/john/ for Mac and Windows.

Because we want to just use a wordlist as is, with no modifications, we can use the "wordlist" mode. This mode will hash every line in the wordlist and check it against our hashes.

The title, Rock You is the name of a popular wordlist of common passwords from a data breach (mentioned in the description). The list I used is included in the default Kali install, but it can also be downloaded here: https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

I used the tool hash-identifier, included with Kali, to detect the hash. It returned the most probable hash type to be md5.

Now that we have the hash type and the wordlist, we can run the following command:

```zsh
john --wordlist=rockyou.txt --format=raw-md5 hashes.txt
```

This returned the following 5 plaintext passwords, which is the flag:
```
saleen94         (?)
kellilayne       (?)
coolabiez        (?)
bANK$123         (?)
MarkBoyd         (?)
```

reading the contents of ~/.john/john.pot also shows us the hash related to each.
```zsh
cat ~/.john/john.pot
```
returns:
```
$dynamic_0$82af6f54b3cb7ff9aea67e3205f67b2d:saleen94
$dynamic_0$77764b9856a7d45dfbffa4bab92c6979:kellilayne
$dynamic_0$8f5be196c116d266ca269705047af8fe:coolabiez
$dynamic_0$2c7541b65ef9974179b31472156af2e9:bANK$123
$dynamic_0$f8926a478274a9db2f63fb9bd2c11c5e:MarkBoyd
```
if we remove "$dynamic_0\$", we are left with each hash and its cooresponding plaintext

```
82af6f54b3cb7ff9aea67e3205f67b2d:saleen94
77764b9856a7d45dfbffa4bab92c6979:kellilayne
8f5be196c116d266ca269705047af8fe:coolabiez
2c7541b65ef9974179b31472156af2e9:bANK$123
f8926a478274a9db2f63fb9bd2c11c5e:MarkBoyd
```