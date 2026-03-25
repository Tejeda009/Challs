from pwn import *

context.log_level="DEBUG"


def hw(x):
    return bin(x).count("1")


r = remote("segreto.challs.olicyber.it",33000)
r.recvlines(2)

for _ in range(10):
    r.recvline()
    sol = [0]*8
    for i in range(256):
        r.sendlineafter(">", str(i))
        data = r.recvline(False).decode().strip()
        res = bytes.fromhex(data)
        for j in range(8):
            if hw(res[j]) > hw(sol[j]):
                sol[j] = res[j]
    ans = bytes(sol).hex()
    r.sendlineafter(">", "g")
    r.sendlineafter("?", ans)

flag = r.recvline(False).decode()
print(flag)
