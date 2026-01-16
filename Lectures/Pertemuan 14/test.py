
#? Nama: Irenia Maisa Kamila
#? NIM: 2506031
#? Kelas: 1B

import pandas as pd

# Membuat DataFrame dari csv
df = pd.read_csv('insurance.csv')
print("DataFrame dari CSV:")
print(df.head())

# Melihat jumlah baris dan kolom
print("\nJumlah baris dan kolom:")
print(df.shape)

csvfile = pd.read_csv("insurance.csv")
dfsort = csvfile.sort_values(by=['sex'])
dfdesc = csvfile.sort_values(by=['sex'], ascending=False)
print("Hasil filter: \n", dfdesc.head())



groupingfile = csvfile.groupby('sex').agg(average_age = ('age', 'mean'),
                                          median_expenses = ('expenses', 'median'))
print("Hasil filter: \n", groupingfile.head())



addcolumn = csvfile['discount_expenses'] = csvfile['expenses']*0.05
print("Hasil filter: \n", csvfile.head())

import csv

inventaris = {}

with open("abc.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        nama = row["nama_barang"]
        stok = int(row["stok"])
        inventaris[nama] = stok

pengiriman = {
    "Pulpen": 20,
    "Buku Tulis": 15,
    "Penghapus": 10
}

penjualan = {
    "Pulpen": 5,
    "Kertas HVS": 30,
    "Stabilo": 8
}


for barang, jumlah in pengiriman.items():
    if barang in inventaris:
        inventaris[barang] += jumlah

for barang, jumlah in penjualan.items():
    if barang in inventaris:
        inventaris[barang] -= jumlah
        if inventaris[barang] < 0:
            inventaris[barang] = 0

with open("stok_akhir.csv", "w") as file:
    file.write("nama_barang, stok_akhir\n")
    for barang, stok in inventaris.items():
        file.write(f"{barang},{stok}\n")

print("Update stok selesai! File 'stok_akhir.csv' telah dibuat.")