from requests import *
r=request("FLAG","http://convenzione.challs.olicyber.it/")
print(r.text)
print(r.headers)