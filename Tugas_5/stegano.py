from PIL import Image
import sys

# ubah byte jadi bit
def ke_bit(data):
    for b in data:
        for i in range(7, -1, -1):
            yield (b >> i) & 1

# ubah bit jadi byte
def dari_bit(bit_list):
    hasil = bytearray()
    temp = 0
    for i, b in enumerate(bit_list):
        temp = (temp << 1) | b
        if (i + 1) % 8 == 0:
            hasil.append(temp)
            temp = 0
    return bytes(hasil)

# masukin bit ke gambar
def sisip_bit(gbr, bit_list):
    px = gbr.load()
    w, h = gbr.size
    bit_list = list(bit_list)
    idx = 0
    for y in range(h):
        for x in range(w):
            if idx >= len(bit_list):
                return gbr
            r, g, b = px[x, y]
            if idx < len(bit_list):
                r = (r & ~1) | bit_list[idx]; idx += 1
            if idx < len(bit_list):
                g = (g & ~1) | bit_list[idx]; idx += 1
            if idx < len(bit_list):
                b = (b & ~1) | bit_list[idx]; idx += 1
            px[x, y] = (r, g, b)
    return gbr

# ambil bit dari gambar
def ambil_bit(gbr, jml_bit):
    px = gbr.load()
    w, h = gbr.size
    hasil = []
    for y in range(h):
        for x in range(w):
            if len(hasil) >= jml_bit:
                return hasil
            r, g, b = px[x, y]
            hasil.append(r & 1)
            if len(hasil) >= jml_bit: break
            hasil.append(g & 1)
            if len(hasil) >= jml_bit: break
            hasil.append(b & 1)
            if len(hasil) >= jml_bit: break
    return hasil

# encode teks
def encode_teks(cover, hasil, pesan):
    print("Mulai encode teks...")
    gbr = Image.open(cover).convert("RGB")
    data = pesan.encode("utf-8")
    panjang = len(data)
    header = panjang.to_bytes(4, "big")
    semua_bit = ke_bit(header + data)
    gbr_baru = sisip_bit(gbr, semua_bit)
    gbr_baru.save(hasil)
    print("Teks disisipkan ke", hasil)

# encode gambar
def encode_gambar(cover, hasil, rahasia):
    print("Mulai encode gambar...")
    gbr = Image.open(cover).convert("RGB")
    with open(rahasia, "rb") as f:
        data = f.read()
    panjang = len(data)
    header = panjang.to_bytes(4, "big")
    semua_bit = ke_bit(header + data)
    gbr_baru = sisip_bit(gbr, semua_bit)
    gbr_baru.save(hasil)
    print(f"Gambar {rahasia} berhasil disisipkan ke {hasil}")

# decode teks
def decode_teks(stegano):
    print("Mulai decode teks...")
    gbr = Image.open(stegano).convert("RGB")
    header_bit = ambil_bit(gbr, 32)
    header_byte = dari_bit(header_bit)
    panjang = int.from_bytes(header_byte, "big")
    semua_bit = ambil_bit(gbr, 32 + panjang * 8)[32:]
    data = dari_bit(semua_bit)
    try:
        teks = data.decode("utf-8")
        print("Pesan tersembunyi:", teks)
    except:
        print("Gagal decode teks, mungkin ini gambar.")

# decode gambar
def decode_gambar(stegano, hasil):
    print("Mulai decode gambar...")
    gbr = Image.open(stegano).convert("RGB")
    header_bit = ambil_bit(gbr, 32)
    header_byte = dari_bit(header_bit)
    panjang = int.from_bytes(header_byte, "big")
    semua_bit = ambil_bit(gbr, 32 + panjang * 8)[32:]
    data = dari_bit(semua_bit)
    with open(hasil, "wb") as f:
        f.write(data)
    print(f"Gambar tersembunyi disimpan ke {hasil}")

# main
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Cara pakai:")
        print("  python stegano.py encode_teks cover.png hasil.png 'Pesan'")
        print("  python stegano.py encode_gambar cover.png hasil.png rahasia.png")
        print("  python stegano.py decode_teks hasil.png")
        print("  python stegano.py decode_gambar hasil.png hasil_decode.png")
        sys.exit()

    perintah = sys.argv[1]

    if perintah == "encode_teks":
        _, _, cover, hasil, teks = sys.argv
        encode_teks(cover, hasil, teks)
    elif perintah == "encode_gambar":
        _, _, cover, hasil, rahasia = sys.argv
        encode_gambar(cover, hasil, rahasia)
    elif perintah == "decode_teks":
        _, _, stegano = sys.argv
        decode_teks(stegano)
    elif perintah == "decode_gambar":
        _, _, stegano, hasil = sys.argv
        decode_gambar(stegano, hasil)
    else:
        print("Perintah tidak dikenal.")
