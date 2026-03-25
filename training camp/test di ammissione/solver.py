
from pwn import remote, context


def solve(stato,mosse):
    solv = ""
    for i in range(len(mosse)):
        for n in mosse[i]:
            while(stato[n] < 5):
                solv += f"{i+1} "
                for j in mosse[i]:
                    stato[j] += 1
    return solv

r = remote("test.challs.olicyber.it", 15004)
r.recvlines(20)

livello = r.recvline()
print(livello.decode())
while livello.startswith(b"Livello"):
    stato = [int(_) for _ in r.recvline(False).decode().split()]
    mosse = []
    while True:
        s = r.recvline(False).decode()
        print(s)
        if s == "":
            break
        mosse.append(["ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(_) for _ in s.split()])
    res = solve(stato,mosse)
    r.sendline(res)
    r.recvlines(2)
    livello = r.recvline(False)
print(livello.decode())