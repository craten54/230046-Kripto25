# 🔐 Kriptografi: Vigenère Cipher & ElGamal

## 📌 Deskripsi
Repository ini berisi implementasi sederhana dari dua algoritma kriptografi klasik dan modern menggunakan **Python**:

1. **Vigenère Cipher** → cipher substitusi polialfabetik klasik.
2. **ElGamal** → skema kriptografi berbasis teori bilangan & logaritma diskret.

Keduanya mendukung **enkripsi** dan **dekripsi**.

---

## ⚡ 1. Vigenère Cipher

### 📖 Penjelasan
- Vigenère menggunakan kunci berupa **string huruf**.
- Setiap huruf plaintext digeser berdasarkan huruf kunci.
- Proses dekripsi dilakukan dengan menggeser huruf sebaliknya.

### 🔑 Rumus
- **Enkripsi**:
  \( C_i = (P_i + K_i) \mod 26 \)
- **Dekripsi**:
  \( P_i = (C_i - K_i) \mod 26 \)

### 🚀 Contoh Penggunaan
```python
msg = "HELLO WORLD"
key = "KEY"

encrypted = encrypt_vigenere(msg, key)
decrypted = decrypt_vigenere(encrypted, key)

print("Plaintext :", msg)
print("Key       :", key)
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)
```

---

## ⚡ 2. ElGamal

### 📖 Penjelasan
- ElGamal merupakan algoritma kriptografi asimetris.
- Berdasarkan teori logaritma diskret dalam grup modulo prima.
- Membutuhkan kunci publik dan kunci privat.

### 🔑 Komponen
- 𝑝 → bilangan prima
- 𝑔 → generator
- 𝑥 → kunci privat (rahasia)
- 𝑦 = 𝑔<sup>𝑥</sup> mod 𝑝 → kunci publik

### 🚀 Proses
- Enkripsi:
  - Pilih bilangan acak 𝑘.
  - Hitung 𝑎 = 𝑔<sup>𝑘</sup> mod 𝑝.
  - Hitung 𝑏 = 𝑀 ⋅ 𝑦<sup>𝑘</sup> mod 𝑝
  - Ciphertext = (𝑎,𝑏).

- Dekripsi:
  - Hitung 𝑀 = 𝑏 ⋅ 𝑎<sup>−𝑥</sup> mod 𝑝

### 🚀 Contoh Penggunaan
``` python
p = 467  # bilangan prima
g = 2    # generator
x = 127  # private key
y = pow(g, x, p)  # public key

message = 123

# Enkripsi
a, b = encrypt_elgamal(message, p, g, y)
print("Ciphertext:", (a, b))

# Dekripsi
decrypted = decrypt_elgamal((a, b), p, x)
print("Decrypted:", decrypted)
```