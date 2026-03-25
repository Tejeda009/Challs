#nella console
#const inviteCode = Array.from({length: 10}, (_, i) => String.fromCharCode(i)).join('');

#fetch('/api/register', {
 # method: 'POST',
  #headers: { 'Content-Type': 'application/json' },
  #body: JSON.stringify({ 
   # username: "tuo_username", 
    #password: "tua_password", 
   # invite: inviteCode 
 # })
#})
#.then(res => res.json())
#.then(data => console.log("Risultato:", data));
import requests

r = requests.post("http://frittomisto.challs.olicyber.it/api/register", json={
    "username": "myusername",
    "password": "mypassword",
    "invite": "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09"
})
print(r.text)