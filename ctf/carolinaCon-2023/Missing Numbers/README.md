Missing Numbers
34 pts

Looks like we have an MD5 hash here. We know the password started with "HackTheCat" and then had 7 numbers.

e443e928a518d1dfdc382239d44d9b8e

Enter the password in the format: flag{Password}


```
./hashcat missingnumbers.hash -a 3 HackTheCat?d?d?d?d?d?d?d

e443e928a518d1dfdc382239d44d9b8e:HackTheCat8923924
```
