# Can You Guess My Favorite Number? (20)
I downloaded the json and dll files, and viewed the json file. It confirmed that the .dll was written with .NET 7.0. I then downloaded dotPeek, a dll decompiler made by JetBrains. I then decompiled it and found C# code, that at the end had a conditional that compared user input to the integer 873867. I then copy and pasted the code into a online C# compiler, and ran it, using 873867 as my input. It then returned the flag.

## Flag
```
CTFWU{wh4t_4_c001_numb3r}
```