ciphertext = "104e137f425954137f74107f525511457f5468134d7f146c4c"
for i in range(256):
    plaintext = bytes([x^i for x in bytes.fromhex(ciphertext)])
    try:
        print(plaintext.decode())
        print("\n")
    except UnicodeDecodeError:
        pass