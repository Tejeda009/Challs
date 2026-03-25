from pwn import *
winaddr=0x40137C
r=remote("gtn2.challs.olicyber.it",10023)
r.interactive()