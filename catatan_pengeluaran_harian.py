import datetime
import random

print("=== Program Catatan Pengeluaran Harian ===")

pengeluaran = []

metode_pembayaran = {"Cash", "Debit", "E-Wallet"}

jumlah = int(input("Berapa kali kamu melakukan pengeluaran hari ini? : "))

for i in range(jumlah):
    ket = input(f"Keterangan pengeluaran ke-{i+1}: ")
    uang = int(input("Nominal (Rp): "))

    print("Metode Pembayaran:")
    for m in metode_pembayaran:
        print("-", m)

    while True:
        metode = input("Pilih metode: ").title()
        if metode in metode_pembayaran:
            break
        else:
            print("Metode tidak tersedia!")

    pengeluaran.append((ket, uang, metode))

print("\nDaftar Pengeluaran hari ini:")
total = 0
for ket, uang, metode in pengeluaran:
    print(ket, ": Rp", uang, "|", metode)
    total += uang

print("\nTotal Pengeluaran : Rp", total)
print("Tanggal :", datetime.date.today())

if total > 1000000:
    print("\nPengeluaranmu cukup boros hari ini!") 
else:
    print("\nPengeluaranmu masih aman hari ini.")

pesan = ["Tetap hemat ya!","Jangan lupa menabung!","Atur pengeluaran dengan baik!"]

print("Reminder :",random.choice(pesan))