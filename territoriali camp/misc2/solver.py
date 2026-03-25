from requests import *
import bs4
re=session()
for i in range(100):
    r=re.get("http://10.45.1.2:8000/") 
    soup=bs4.BeautifulSoup(r.text,"html.parser")
    eq=soup.find(attrs={'class':'fs-4'}).text.split(" ")
    result=int(eq[4])-int(eq[2])
    result=str(round(result/int(eq[0].replace('x'," ")),2))
    print(re.post("http://10.45.1.2:8000/solve",json={'solution':result}).text)
    
print(re.get("http://10.45.1.2:8000/").text)
