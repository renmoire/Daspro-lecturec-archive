
# ! Nama: Irenia Maissa Kamila
# ! NIM: 2506031
# ! Kelas: 1B

jam = int(input("Jam: "))
menit = int(input("Menit: "))

durasi = int(jam * 60 + menit) # dalam menit

if durasi <= 90:
    harga = 5000
else:
    if durasi <= 240:
        sisamenit = durasi - 90
        tambahanmenit = sisamenit // 30
        if sisamenit % 30 != 0: 
            tambahanmenit += 1
        harga = 5000 + (tambahanmenit * 2000)
    else:
        sisamenit = durasi - 240
        tambahanmenitlebih = sisamenit // 30
        if sisamenit % 30 != 0:
            tambahanmenitlebih += 1
        harga = 5000 + (2000 * 5) + (tambahanmenitlebih * 1000)

print(f"\nTotal waktu: {jam} jam {menit} menit")
print(f"Total harga: Rp{harga}")