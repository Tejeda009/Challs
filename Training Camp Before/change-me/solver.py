from requests import *
r=post("http://change-me.challs.olicyber.it/")
print(r.text)