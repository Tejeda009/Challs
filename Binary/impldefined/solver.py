flag=bytearray.fromhex("95637F9D33B2D9573CE334EC7063302CB69F4470A0BE78F7B90000")
xorkey=bytearray.fromhex("F3 0F 1E FA 48 83 EC 08  48 8B 05 D9 2F 00 00 48 85 C0 74 02 FF D0 48 83  C4")
for i in range(25):
    flag[i]^=xorkey[i]
print(flag)