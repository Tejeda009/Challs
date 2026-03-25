from pwn import *
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES,DES
URL="crypto-07.challs.olicyber.it"
port=30000
r=remote(URL,port)
r.recvuntil(b'\nCipher = ')
cipher=r.recvline().strip().decode()
r.recvuntil(b'Mode of operation = ')
mode=r.recvline().strip().decode()
r.recvuntil(b'key.hex() = ')
key=r.recvline().strip().decode()
r.recvuntil(b'plaintext = ')
plaintext=r.recvline().strip().decode()
r.recvuntil(b'Padding scheme =')
padding=r.recvline().strip().decode()
plaintext=pad(plaintext,8,padding)
if cipher=="CBC":
    if mode=="AES":
        cipher=AES.new(bytes.fromhex(key),AES.MODE_CBC)
else:
        cipher=DES.new(bytes.fromhex(key),DES.MODE_CBC)
r.sendline( cipher.encrypt(plaintext).hex())
