flag=bytearray.fromhex("27 2D 20 26 3A 36 29 70  2D 72 70 1E 39 71 33 3C")
key=bytearray.fromhex("F8 6F 86 83 C3 9C 8B 35  F0 C0 87 92 2E 41 2B 53")
dec = bytearray(16)
def rotate(key):
    v1 = bytearray(16)
    v2 = key[0]
    for i in range(0, 15):
        v1[i] = key[i+1]
    v1[15] = v2
    return v1
for i in reversed(range(16)):
    key = rotate(key)
    for j in reversed(range(16)):
        flag[j] ^= key[j]
print(flag.decode())  