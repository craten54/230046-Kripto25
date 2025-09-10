import numpy as np

def mod_inverse(a, m):
    """Cari invers modular dengan Extended Euclidean Algorithm"""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("Tidak ada invers")

def matrix_mod_inverse(matrix, modulus):
    """Cari invers matriks mod 26"""
    det = int(round(np.linalg.det(matrix)))  # determinan asli
    det_mod = det % modulus
    det_inv = mod_inverse(det_mod, modulus)  # invers determinan

    # adjoint matrix
    matrix_adj = np.round(det * np.linalg.inv(matrix)).astype(int)
    inv_matrix = (det_inv * matrix_adj) % modulus
    return inv_matrix

def hill_encrypt(text, K):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += "X"  # padding jika ganjil
    result = ""
    for i in range(0, len(text), 2):
        pair = np.array([[ord(text[i]) - 65], [ord(text[i+1]) - 65]])
        cipher_pair = np.dot(K, pair) % 26
        result += chr(cipher_pair[0,0] + 65) + chr(cipher_pair[1,0] + 65)
    return result

def hill_decrypt(cipher, K):
    K_inv = matrix_mod_inverse(K, 26)
    result = ""
    for i in range(0, len(cipher), 2):
        pair = np.array([[ord(cipher[i]) - 65], [ord(cipher[i+1]) - 65]])
        plain_pair = np.dot(K_inv, pair) % 26
        result += chr(int(plain_pair[0,0]) + 65) + chr(int(plain_pair[1,0]) + 65)
    return result

if __name__ == "__main__":
    K = np.array([[7, 6],
                  [2, 5]])

    plaintext = "PYTHON"
    print("Plaintext :", plaintext)

    cipher = hill_encrypt(plaintext, K)
    print("Encrypted :", cipher)

    decrypted = hill_decrypt(cipher, K)
    print("Decrypted :", decrypted)

    print("Inverse Key Matrix (mod 26):")
    print(matrix_mod_inverse(K, 26))
