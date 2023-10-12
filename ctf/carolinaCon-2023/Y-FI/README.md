Y-FI
91 pts

Looks like we have a PMKID from a WiFi network. We know the password started with "elegantship" and then had 3 numbers.

Enter the password in the format: flag{Password}

```
./hashcat -m 16800 NETGEAR28.pmkid -a 3 elegantship?d?d?d

8cc4e5d6825b7407099b5a8153c4d36c*6ccdd61227c1*b827eb378112*4e4554474541523238:elegantship223
```
