from requests import *
URL="http://gabibbo-says.challs.olicyber.it/"
r=post(URL,data={"gabibbo":"angry"})
print(r.text)