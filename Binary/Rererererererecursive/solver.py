key = (pow(2,64)-1).to_bytes(8,'little')
flag = bytearray.fromhex("99  93 9E 98 84 9E 9B CF 8D CF 97 A0 93 CB A0  8D CC 9C 8A 8D 8C 96 90 91 9A A0 CF CF 9B  C7 CA 99 CD C9 9D 9E CB 9D C8 9C CA 9D C6  99 C9 9D 9C CC CC  9C 9D C8 CE CD C8 C6 99 C6 C8 CA 9C C9 9B  9C CE CF 82" )
dec = bytearray()
for i in range(len(flag)):
    dec.append(flag[i] ^ key[i % 8])
print(dec.decode())