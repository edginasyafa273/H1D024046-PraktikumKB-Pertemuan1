import random
from datetime import datetime

print("=== Sistem Pemesanan Bunga Florist ===")

# Tuple (info toko)
info_toko = ("Florist Indah", "Jl. Melati No. 5", "08:00 - 20:00")

print("\nInformasi Toko:")
print("Nama Toko :", info_toko[0])
print("Alamat    :", info_toko[1])
print("Jam Buka  :", info_toko[2])

# Struktur Data List
bunga = ["Mawar", "Tulip", "Lily", "Peony"]
harga = [20000, 30000, 25000, 40000]
stok  = [50, 30, 40, 20]

# Set
metode_bayar = {"Tunai", "Transfer", "QRIS"}

print("\nDaftar Bunga:")
for i in range(len(bunga)):
    print(f"{i+1}. {bunga[i]} - Rp{harga[i]} (Stok: {stok[i]})")

# Input pilihan
pilihan = int(input("\nPilih nomor bunga: "))
jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))

# Struktur kontrol
if pilihan >= 1 and pilihan <= len(bunga):

    index = pilihan - 1
    nama_bunga = bunga[index]
    harga_bunga = harga[index]
    stok_bunga = stok[index]

    # Cek stok
    if jumlah > stok_bunga:
        print("Maaf, stok bunga tidak mencukupi")
    else:

        total = harga_bunga * jumlah

        # Diskon
        if jumlah >= 5:
            diskon = total * 0.1
        else:
            diskon = 0

        total_bayar = total - diskon

        # Pilih metode pembayaran
        print("\nMetode Pembayaran Tersedia:")
        for metode in metode_bayar:
            print("-", metode)

        bayar = input("Pilih metode pembayaran: ")

        # Library datetime
        waktu = datetime.now()

        # Library random
        nomor_pesanan = random.randint(1000, 9999)

        # Update stok
        stok[index] -= jumlah

        print("\n=== STRUK PEMBELIAN ===")
        print("Nomor Pesanan :", nomor_pesanan)
        print("Tanggal       :", waktu.strftime("%d-%m-%Y %H:%M"))
        print("Bunga         :", nama_bunga)
        print("Jumlah        :", jumlah)
        print("Harga Satuan  :", harga_bunga)
        print("Total Harga   :", total)
        print("Diskon        :", diskon)
        print("Total Bayar   :", total_bayar)
        print("Metode Bayar  :", bayar)
        print("Sisa Stok     :", stok[index])

else:
    print("Pilihan bunga tidak tersedia")