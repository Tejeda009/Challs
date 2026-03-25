from requests import *

headers={
    'give-me':'the-flag',
    'Cookie':'session_id=the_session',
    'Content-Type':'text/plain'
}
data='pretty please :('
r=options("http://10.45.1.2:4001?we_like=flags",headers=headers,data=data)
print(r.text)