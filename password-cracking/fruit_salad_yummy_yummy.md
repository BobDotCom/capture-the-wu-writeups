Fruit Salad, Yummy Yummy
20
Question: A member of your team has gone through some old documents and found some odd hashes that seem to have a common theme. Can you decrypt them?

53d29fd4dbd7c1420a5aa6eee66a24a6 d3a03fd7b54942e6a8910bad62aa191b 0c36e06c538f8412da18195e3dde1d9b 927a25e9fe0d30f55c7dafefb8d8f642 570b1025c866233c37a015b9f24996b4

I identified all of the hashes as md5 and ran john with the provided wordlist and all default kali wordlists. 

we cracked the following hashes:
53d29fd4dbd7c1420a5aa6eee66a24a6:applepiez458
570b1025c866233c37a015b9f24996b4:strawberryshortcake12

We then looked at what was in common.
- fruit, dessert, number/character.

We created our own wordlist with a combination of every fruit and dessert we could think of, followed by fuzzing characters at the end. We also tried different capitalization and plurality. We werent able to crack any more hashes.