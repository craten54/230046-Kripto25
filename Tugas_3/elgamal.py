import random

# Algoritma Euclidean untuk gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Cari invers modulo
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Fast exponentiation (modular exponentiation)
def power(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

# Generate key
def generate_keys():
    p = 427
    g = 3
    x = random.randint(1, p - 2)  # private key
    y = power(g, x, p)            # public key
    return (p, g, y), x           # (public, private)

# Enkripsi satu angka
def encrypt_number(public_key, m):
    p, g, y = public_key
    k = random.randint(1, p - 2)
    a = power(g, k, p)
    b = (m * power(y, k, p)) % p
    return (a, b)

# Dekripsi satu angka
def decrypt_number(private_key, public_key, ciphertext):
    p, g, y = public_key
    a, b = ciphertext
    s = power(a, private_key, p)
    s_inv = modinv(s, p)
    m = (b * s_inv) % p
    return m

# Enkripsi umum (angka atau string)
def encrypt(public_key, message):
    if isinstance(message, int):
        return encrypt_number(public_key, message)
    elif isinstance(message, str):
        return [encrypt_number(public_key, ord(ch)) for ch in message]
    else:
        raise TypeError("Message harus int atau str")

# Dekripsi umum (angka atau string)
def decrypt(private_key, public_key, ciphertext):
    if isinstance(ciphertext, tuple):
        return decrypt_number(private_key, public_key, ciphertext)
    elif isinstance(ciphertext, list):
        return ''.join(chr(decrypt_number(private_key, public_key, c)) for c in ciphertext)
    else:
        raise TypeError("Ciphertext harus tuple atau list")

# Contoh penggunaan
public_key, private_key = generate_keys()
print("\nElGamal Cipher")
print("Public Key :", public_key)
print("Private Key:", private_key)

# Pesan numerik
message_num = 123
cipher_num = encrypt(public_key, message_num)
decrypted_num = decrypt(private_key, public_key, cipher_num)
print("\n=== Numerik ===")
print("Plaintext :", message_num)
print("Encrypted :", cipher_num)
print("Decrypted :", decrypted_num)

# Pesan string
message_str = "EZKRIPTOGRAFI"
cipher_str = encrypt(public_key, message_str)
decrypted_str = decrypt(private_key, public_key, cipher_str)
print("\n=== String ===")
print("Plaintext :", message_str)
print("Encrypted :", cipher_str)
print("Decrypted :", decrypted_str)
