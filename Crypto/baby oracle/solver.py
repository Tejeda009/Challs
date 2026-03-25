from pwn import *
from Crypto.Util.number import inverse, long_to_bytes
from math import gcd

# --- CONFIGURAZIONE ---
# Sostituisci con l'indirizzo del servizio
HOST = 'babyoracle.challs.olicyber.it' 
PORT = 12007

# Se vuoi testare in locale (avendo il file originale), scommenta qui:
# r = process(['python3', 'babyoracle.py'])
r = remote(HOST, PORT)

# 1. Recuperiamo i parametri pubblici
r.recvuntil(b"n = ")
n = int(r.recvline().strip())
print(f"[+] Ricevuto N: {n}")

r.recvuntil(b"encrypted flag = ")
enc_flag = int(r.recvline().strip())
print(f"[+] Ricevuta Flag Cifrata: {enc_flag}")

# 2. Scegliamo un ciphertext arbitrario da inviare all'oracolo
# Deve essere diverso dalla flag cifrata. 2 va benissimo.
ct_chosen = 2
e = 65537

# 3. Interroghiamo l'oracolo
r.recvuntil(b"Give me something to decrypt: ")
r.sendline(str(ct_chosen).encode())

# 4. Riceviamo la risposta parziale (ct^dp mod p)
partial_dec = int(r.recvline().strip())
print(f"[+] Risposta Oracolo (m_p): {partial_dec}")

# 5. Attacco matematico per recuperare P
# Sappiamo che: partial_dec^e - ct_chosen = k * p
# Quindi GCD(partial_dec^e - ct_chosen, n) ci darà p
val = pow(partial_dec, e, n) # Calcoliamo in modulo n per efficienza
p = gcd(val - ct_chosen, n)

if p == 1 or p == n:
    print("[-] Errore: Fattorizzazione fallita.")
    exit()

print(f"[+] Fattore P trovato: {p}")

# 6. Ricostruzione della chiave privata
q = n // p
phi = (p - 1) * (q - 1)
d = inverse(e, phi)

# 7. Decifratura della flag
m = pow(enc_flag, d, n)
flag = long_to_bytes(m)

print("\n" + "="*30)
print(f"FLAG: {flag.decode(errors='ignore')}")
print("="*30)

r.close()