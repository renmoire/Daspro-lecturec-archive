
#? Nama: Irenia Maisa Kamila
#? NIM: 2506031
#? Kelas: 1B

import csv

gudang = {}

with open("inventaris_barang.csv", "r") as file:
    dataframe = csv.reader(file)
    for item in dataframe:
        if len(item) < 2:
            continue

        nama = item[0]
        jumlah = int(item[1])

        gudang[nama] = jumlah


barang = input("Nama barang: ").lower()
perubahan = int(input("Perubahan: "))

ditemukan = False

for nama in gudang:
    if nama.lower() == barang:
        gudang[nama] += perubahan
        print("Berhasil")
        ditemukan = True
        break

if not ditemukan:
    print("Barang tidak ditemukan")


with open("inventaris_barang.csv", "w", newline="") as file:
    update = csv.writer(file)
    for barang, jumlah in gudang.items():
        update.writerow([barang, jumlah])


print("\nDATA TERBARU")
for barang, jumlah in gudang.items():
    print(f"Nama: {barang}")
    print(f"Jumlah: {jumlah}\n")