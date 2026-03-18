import random
import datetime

print("=== Sistem Catatan Pengeluaran Harian ===")

# Tuple (info pengguna)
info_user = ("Edgina", "Mahasiswa", "Keuangan Harian")

print("\nInformasi Pengguna:")
print("Nama     :", info_user[0])
print("Status   :", info_user[1])
print("Program  :", info_user[2])

# List untuk menyimpan data
pengeluaran = []

# Set metode pembayaran
metode_bayar = {"Cash", "Debit", "E-Wallet"}

# Input jumlah pengeluaran
while True:
    try:
        jumlah = int(input("\nBerapa kali pengeluaran hari ini? : "))
        if jumlah > 500:
            print("Jumlah terlalu banyak! Coba lagi.")
        elif jumlah == 0:
            print("Tidak ada pengeluaran hari ini.")
            exit()
        if jumlah < 0:
            break
            print("Jumlah tidak boleh negatif!")
    except:
        print("Masukkan angka yang benar!")


# Input data pengeluaran
for i in range(jumlah):
    print(f"\nPengeluaran ke-{i+1}")
    
    # Validasi kategori (harus huruf)
    while True:
        kategori = input("Kategori pengeluaran: ")
        if kategori.isalpha():
            break
        else:
            print("Kategori harus berupa huruf!")

    # Validasi nominal
    while True:
        try:
            uang = int(input("Nominal (Rp): "))
            if uang > 0:
                break
            else:
                print("Nominal harus lebih dari 0!")
        except:
            print("Masukkan angka yang benar!")

    # Pilih metode pembayaran
    print("Metode Pembayaran:")
    for m in metode_bayar:
        print("-", m)

    # Validasi metode pembayaran
    while True:
        bayar = input("Pilih metode: ").title()
        if bayar in metode_bayar:
            break
        else:
            print("Metode tidak tersedia!")

    # Simpan ke list (tuple)
    pengeluaran.append((kategori, uang, bayar))

# Proses & tampilkan data
total = 0

print("\n=== STRUK PENGELUARAN ===")
for data in pengeluaran:
    print("Kategori :", data[0])
    print("Nominal  : Rp", data[1])
    print("Metode   :", data[2])
    print("---------------------")
    total += data[1]

# Status pengeluaran
if total > 100000:
    status = "Boros"
elif total > 50000:
    status = "Cukup"
else:
    status = "Hemat"

# Waktu
waktu = datetime.now()

# Output akhir
print("\n=== RINGKASAN ===")
print("Tanggal      :", waktu.strftime("%d-%m-%Y %H:%M"))
print("Total        : Rp", total)
print("Status       :", status)

# Pesan random
pesan = [
    "Pengeluaranmu terkendali!",
    "Ayo lebih hemat lagi!",
    "Jangan lupa menabung!"
]

print("Pesan :", random.choice(pesan))