from pwn import *

# Parametri del server remoto
HOST = 'spg.challs.olicyber.it'
PORT = 38052

def solve():
    # Connessione al servizio
    try:
        io = remote(HOST, PORT)
    except Exception as e:
        print(f"Errore di connessione: {e}")
        return

    def get_menu():
        return io.recvuntil(b'> ')

    # 1. Registriamo l'utente "admin"
    # È necessario perché il token decifrato dovrà contenere un username presente in 'users'
    print("[*] Fase 1: Registrazione utente 'admin'...")
    get_menu()
    io.sendline(b'1')
    io.recvuntil(b'Username? ')
    io.sendline(b'admin')
    io.recvline() # Salta la passphrase generata casualmente
    io.recvline() # Salta la riga del token

    # 2. Creazione del payload per l'iniezione
    # Struttura token: username=[USER];index0=X;index1=Y...
    # Iniettiamo i nostri indici desiderati (0,1,2,3) nello username.
    # Usiamo un padding per allineare il ';' del server all'inizio di un nuovo blocco AES.
    
    # "username=" (9 byte) + "admin" (5 byte) + injection (37 byte) = 51 byte.
    # Per arrivare a 64 byte (fine del Blocco 3), aggiungiamo 13 'A'.
    # Il ';' del server inizierà al byte 64 (Blocco 4).
    injection = "admin;index0=0;index1=1;index2=2;index3=3"
    padding = "A" * 13
    payload_username = injection + padding
    
    print(f"[*] Fase 2: Generazione token malevolo per {payload_username}...")
    get_menu()
    io.sendline(b'1')
    io.recvuntil(b'Username? ')
    io.sendline(payload_username.encode())
    
    io.recvline() # Passphrase (inutile)
    token_line = io.recvline().decode()
    token_hex = token_line.strip().split(': ')[1]
    token_bytes = bytearray.fromhex(token_hex)

    # 3. Bit Flipping Attack
    # Token = IV (16) + C0 (16) + C1 (16) + C2 (16) + C3 (16) + ...
    # Il Blocco 4 di plaintext (P4) inizia al byte 64. Qui si trova il ';' del server.
    # Per modificare P4[0], dobbiamo fare XOR su C3[0].
    # C3 inizia all'indice 16 (IV) + 3*16 = 64 del token.
    
    target_pos = 64 
    # Trasformiamo ';' (0x3b) in 'X' (0x58) per rompere il parsing del server
    token_bytes[target_pos] ^= (ord(';') ^ ord('X'))
    
    forged_token = token_bytes.hex()
    print("[*] Fase 3: Token manipolato con successo.")

    # 4. Recupero della Passphrase (FLAG)
    print("[*] Fase 4: Invio token per il recupero dei blocchi della flag...")
    get_menu()
    io.sendline(b'2')
    io.recvuntil(b'Token? ')
    io.sendline(forged_token.encode())
    
    try:
        result = io.recvline().decode()
        if "La tua passphrase è" in result:
            passphrase = result.split(" è ")[1].strip()
            # La flag è composta dai 4 blocchi uniti. Rimuoviamo il separatore '-'
            flag = passphrase.replace("-", "")
            print("\n" + "="*40)
            print(f"CONGRATULAZIONI! Flag trovata:\n{flag}")
            print("="*40)
        else:
            print(f"[-] Errore: Il server ha risposto: {result}")
    except EOFError:
        print("[-] Il server ha chiuso la connessione. Probabile errore nel parsing del token.")

    io.close()

if __name__ == "__main__":
    solve()