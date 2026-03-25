import requests

r = requests.post("http://frittomisto.challs.olicyber.it/api/register", json={
    "username": "myusername13",
    "password": "mypassword13",
    "invite": "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09"
})
print(r.text)