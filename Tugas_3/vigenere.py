# Vigenere Cipher

def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return "".join(key)
    else:
        return "".join(key[i % len(key)] for i in range(len(text)))

def encrypt_vigenere(plaintext, key):
    ciphertext = []
    key = generate_key(plaintext, key)
    for p, k in zip(plaintext, key):
        if p.isalpha():
            shift = (ord(p.upper()) + ord(k.upper())) % 26
            ciphertext.append(chr(shift + 65))
        else:
            ciphertext.append(p)
    return "".join(ciphertext)

def decrypt_vigenere(ciphertext, key):
    plaintext = []
    key = generate_key(ciphertext, key)
    for c, k in zip(ciphertext, key):
        if c.isalpha():
            shift = (ord(c.upper()) - ord(k.upper()) + 26) % 26
            plaintext.append(chr(shift + 65))
        else:
            plaintext.append(c)
    return "".join(plaintext)

# Contoh
msg = "ASPRAKGANTENG"
key = "STAN"
encrypted = encrypt_vigenere(msg, key)
decrypted = decrypt_vigenere(encrypted, key)

print("Vigenere Cipher")
print("Plaintext :", msg)
print("Key       :", key)
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)
