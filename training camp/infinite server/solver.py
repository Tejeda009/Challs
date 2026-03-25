from bs4 import BeautifulSoup
import requests
session = requests.Session()
doc = session.get("http://infinite.challs.olicyber.it").text
soup = BeautifulSoup(doc, "html.parser")
while (True):
    if (soup.center.h2.text=="GRAMMAR TEST"):
        txt = soup.center.p.text
        char = txt[8:9]
        word = txt[txt.find('"', 12, len(txt))+1:-2]
        soup = BeautifulSoup(session.post(url = "http://infinite.challs.olicyber.it", headers = {"Content-Type": "application/x-www-form-urlencoded"}, data = "letter="+str(word.count(char))+"&submit=Submit").text, "html.parser")
    elif (soup.center.h2.text=="MATH TEST"):
        txt = soup.center.p.text.replace("Quanto fa ", "")
        num1, num2 = txt[:-1].split(" + ")
        num1, num2 = int(num1), int(num2)
        soup = BeautifulSoup(session.post(url = "http://infinite.challs.olicyber.it", headers = {"Content-Type": "application/x-www-form-urlencoded"}, data = "sum="+str(num1+num2)+"&submit=Submit").text, "html.parser")
    elif (soup.center.h2.text=="ART TEST"):
        color = soup.center.p.text.replace("Premi il pulsante di colore ", "")[:-1]
        soup = BeautifulSoup(session.post(url = "http://infinite.challs.olicyber.it", headers = {"Content-Type": "application/x-www-form-urlencoded"}, data = color+"="+"&submit=Submit").text, "html.parser")
    else:
        print(soup.center.p.text)
        break
