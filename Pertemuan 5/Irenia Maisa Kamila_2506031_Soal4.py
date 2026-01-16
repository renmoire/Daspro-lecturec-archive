# Nama: Irenia Maisa Kamila
# NIM: 2506031
# Kelas: 1B
# Paket soal 1C




mobil ={
    "Merk": "Honda",
    "Tipe": "HRV",
    "Tahun": 2018,
    "Warna": "Hitam",
    "No. Polisi": "D 1234 ABC",
    "Bensin": "Pertalite",
    "Tranmisi": "Manual"
}

print("-"*30)
print("Diketahui mobil lama Pak Oki:")
for kiri, kanan in mobil.items():
    print(f"    {kiri}: {kanan}")

mobilbaru = {}

print("-"*30)
print("Silakan lengkapi data di bawah ini untuk menginput detail mobil baru Pak Oki")

for kiri, kanan in mobil.items():
    baru = input(f"{kiri}: ")
    mobilbaru[kiri] = baru

print("-"*30)
print("Mobil baru Pak Oki adalah:")
for kiri, kanan in mobilbaru.items():
    print(f"    {kiri}: {kanan}")