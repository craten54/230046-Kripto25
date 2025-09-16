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
    p = 37 # bilangan prima
    g = 3   # generator
    x = random.randint(1, p-2) # private key
    y = power(g, x, p)         # public key
    return (p, g, y), x        # (public, private)

# Enkripsi
def encrypt(public_key, m):
    p, g, y = public_key
    k = random.randint(1, p-2)
    a = power(g, k, p)
    b = (m * power(y, k, p)) % p
    return (a, b)

# Dekripsi
def decrypt(private_key, public_key, ciphertext):
    p, g, y = public_key
    a, b = ciphertext
    s = power(a, private_key, p)
    s_inv = modinv(s, p)
    m = (b * s_inv) % p
    return m

# Contoh penggunaan
public_key, private_key = generate_keys()
print("\nElGamal Cipher")
print("Public Key :", public_key)
print("Private Key:", private_key)

message = 123  # pesan numerik
ciphertext = encrypt(public_key, message)
decrypted = decrypt(private_key, public_key, ciphertext)

print("Plaintext  :", message)
print("Encrypted  :", ciphertext)
print("Decrypted  :", decrypted)
