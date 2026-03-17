import datetime
import random

print("=== Program Catatan Pengeluaran Harian ===")

pengeluaran = []

jumlah = int(input("Berapa kali kamu melakukan pengeluaran hari ini? : "))

for i in range(jumlah):
    ket = input(f"Keterangan pengeluaran ke-{i+1}: ")
    uang = int(input("Nominal (Rp): "))
    pengeluaran.append((ket, uang))

print("\nDaftar Pengeluaran hari ini:")
total = 0
for ket, uang in pengeluaran:
    print(ket, ": Rp", uang)
    total += uang

print("\nTotal Pengeluaran : Rp", total)
print("Tanggal :", datetime.date.today())

pesan = ["Tetap hemat ya!","Jangan lupa menabung!","Atur pengeluaran dengan baik!"]

print(random.choice(pesan))