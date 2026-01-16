# Nama: Irenia Maisa Kamila
# NIM: 2506031
# Kelas: 1B
# Paket soal 1C



barang = [
    "T-Shirt", "Blouse", "Kemeja", 
    "Celana Panjang", "Rok", "Baju Renang", 
    "Tas", "Topi", "Sepatu", 
    "Sendal"
]


jumlahjenisbarangjuli = len(barang)

print("-"*70)
print("List barang lama di bulan juli:")
for isi in barang:
    print(f"- {isi}")
    
print(f"Total jenis barangnya adalah {jumlahjenisbarangjuli} jenis")



print("-"*70)
print("Di bulan sekarang, toko Nabila berhenti menjual topi dan menggantikannya dengan dompet dan menambahkan Jepitan Rambut & Kerudung karena banyak peminatnya.")
barangpengganti =  "Dompet"
barangtambahan = "Jepitan Rambut"
barangtambahan2 = "Kerudung"
semuabarangtambahan = [barangtambahan, barangtambahan2]

barang[7] = barangpengganti
barang.append(semuabarangtambahan)

for isi in barang:
    print(f"- {isi}")

jumlahjenisbarangsekarang = len(barang)
print(f"Total jenis barang bulan sekarang adalah {jumlahjenisbarangsekarang} jenis")