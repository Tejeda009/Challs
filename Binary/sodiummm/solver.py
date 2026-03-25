
from hashlib import sha512


xorkey=("tung tung tung sahur VS cappuccino assassino")
flag=bytearray.fromhex("2CE4190BDF7C920301217B56B11F067FD361BB2F11B04E7B9A75912B16ADB5AF96E00ED7ECBCB1FC5CF80837AC4F40D181C0CDF9B8167CE2F982AC6A6F9035F2")
real=""
hashed = bytearray.fromhex(sha512(xorkey.encode()).hexdigest())
for i in range(len(flag)):
    flag[i]^=hashed[i % len(hashed)]

for i in range(0, len(flag), 2):
    flag[i] ^= 0x20
print(flag) 