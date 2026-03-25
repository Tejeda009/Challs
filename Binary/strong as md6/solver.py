flag=bytearray.fromhex("67 7C EA 32 8B C0 C6 9F  DA D7 E8 1C D3 F6 AF B5")
table=bytearray.fromhex("AD F7 B1 83 60 53 B7 5E  44 91 55 4B BC FB 85 5B 3F EC 55 D5 21 E3 B1 A9  15 C9 90 48 C2 25 2E 30 06 B3 A6 E4 F5 AC 7E 12  AD 6B C2 82 BF 0D 8A 2A0F 7A DD 8F 9A AE 68 14  A4 A6 D5 D7 20 96 00 00")
for i in range(4):
    for j in range(16):
        print(table[16*i+j])
        result = flag[j] -table[16*i+j]
        if result < 0:
            result += 256
        flag[j] = result
print(flag)