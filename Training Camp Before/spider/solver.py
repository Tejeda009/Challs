
import requests

url = "http://spider.challs.olicyber.it/"
headers = {
    'User-Agent': 'Googlebot'
}

response = requests.get(url, headers=headers)
print(response.text)