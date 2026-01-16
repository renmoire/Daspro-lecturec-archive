# Nama: Irenia Maisa Kamila
# NIM: 2506031
# Kelas: 1B

namakota = ("Jakarta", "Bandung", "Surabaya")
koordinat = (-6.2088, 106.8456), (-6.9175, 107.6191), (-7.2575, 112.7521)

kotabandung = f"==================================\nKota: {namakota[1]}\nKoordinat: {koordinat[1]}"
print(kotabandung)



print("==================================\nJumlah data yang tersimpan")
print(len(namakota))



kotanya = int(input("==================================\n1. Jakarta\n2. Bandung\n3. Surabaya\nKota yang kamu inginkan (1-3): "))



index = kotanya - 1
nyatu = f"====================================\nKota: {namakota[index]}\nKoordinat: {koordinat[index]}"
print(nyatu)
