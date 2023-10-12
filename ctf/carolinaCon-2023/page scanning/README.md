# Challenge text:

Shit, our admin got drunk again and forgot the endpoint on our new webpage and now we are locked out of the server. They can only remember that the page was on a server at 192.81.216.59 and had 3 of the words below in the path, like this http://192.81.216.59/test.page.here/

Can you find that webpage? Flag format will be flag{word1.word2.word3}

cat paper hack steel robot strike bottle mute drum static horse cherry storm

192.81.216.59

---

Used ffuf to scan the site using the provided words as a dictionary, and find the hidden endpoint:



```console
┌──(kali㉿kali)-[~]
└─$ cat page-scanning-carolinaCon2023 
cat
paper
hack
steel
robot
strike
bottle
mute
static
horse 
storm
                                                                                                                                       
┌──(kali㉿kali)-[~]
└─$ ffuf -v -w page-scanning-carolinaCon2023:W1 -w page-scanning-carolinaCon2023:W2 -w page-scanning-carolinaCon2023:W3 -u http://192.81.216.59/W1.W2.W3/ 

```
![PageScanning-flag](https://user-images.githubusercontent.com/1743650/234162263-19c6083f-7b93-437c-9cce-56c8e1175ede.png)

