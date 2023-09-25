# Gotta Catch em All - 20 Points
## Description
Our team has found a set of encrypted messages. They seemed to have figured out that the passwords consists of a pokemon followed by some numbers. Can you decrypt them?

Hashes:

fbf5496a008165f6db865a23b3da8d89 8d4244cb30f5aff30b2327eb439dea05 3c19b01733e53bd0bf860c59aa2c1c6f ba351835bcc91d880881d05725ae399d ff097d17d99af6a74612e9d2784be70d

## Solution

To crack these passwords, I used the tool "John the Ripper." More about this is specified in the "RockYou.md" writeup.

I found the hash format to be md5 using hash-identifier.

The description clearly states that the passwords would be a name of a pokemon followed by some numbers. To start, I got a wordlist of pokemon names here:
https://github.com/cervoise/pentest-scripts/blob/master/password-cracking/wordlists/pokemon-list-en.txt

John has a feature where you can apply rules to a wordlist with --rules to modify each word in a certain way. I created a ruleset in the file "~/.john/john.conf" by adding the following:
```
[List.Rules:Example]
Az"[0-9]"
Az"[0-9][0-9]"
Az"[0-9][0-9][0-9]"
Az"[0-9][0-9][0-9][0-9]"
Az"[0-9][0-9][0-9][0-9][0-9]"
```

I learned how to format this ruleset from this article:
https://akimbocore.com/article/custom-rules-for-john-the-ripper/

To paraphrase,"Az" specifies that we want to append the following to the end of each word. What exactly we want to append is "some numbers" stated by the challenge description. To specify a number 0-9, we put "[0-9]." For more digits, simply repeat "[0-9]". Because I was unsure of how many numbers, I tried 1-5 just to be safe.

Now that we have the wordlist, and our rules to add "some numbers" to the end. We can run the command:
```zsh
john --wordlist=pokemonList.txt --rules=Example --format=raw-md5 hashes.txt
```

This returned the following, which was the flag:
```
dratini13        (?)
gengar420        (?)
golduck467       (?)
pikachu866       (?)
charizard13478   (?)
```

-Hudson