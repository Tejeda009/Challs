from pwn import *
r=remote("2048.challs.olicyber.it",10007)
i=r.recvline().decode().strip()
print(i)
print(r.recvline().decode().strip())
while i.find('flag')==-1: 
    try:
        op=r.recvuntil(b' ').decode().strip()
        print(op)
        num1=int(r.recvuntil(b' ').decode().strip(),10)
        print(num1)
        num2=int(r.recvuntil(b' ').decode().strip(),10)
        print(num2)
        res=''
        if op=='POTENZA':
            res=str(num1**num2)
        elif op=='PRODOTTO':
            res=str(num1*num2)
        elif op=='DIVISIONE':
            res=str(num1/num2)
        elif op=='SOMMA':
            res=str(num1+num2)
        elif op=='DIFFERENZA':
            res=str(num1-num2)
        elif op=='DIVISIONE_INTERA':
            res=str(num1//num2)
        print(res)
        r.sendline(res.encode())
    except:
        print(r.recvline().decode().strip())