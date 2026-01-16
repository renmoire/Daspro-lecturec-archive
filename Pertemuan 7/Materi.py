
#! Nama: Irenia Maisa Kamila
#! NIM: 2506031
#! Kelas: 1B

coba = 3
for isi in range(coba):
    print(f"Perulangan ke-{isi}")

for isi in "Coba":
    print(f"Huruf: {isi}")

for isi in range (1,4):
    print(isi)


buah = ["Apel", "Jeruk", "Manggis"]
for isi in buah:
    print(f"Buah: {isi}")

for isi in range(len(buah)):
    print(isi)



angka = 1
while(angka < 3):
    print(f"Angka sekarang: {angka}")
    angka += 1


buah = ["Apel", "Jeruk", "Manggis"]
x = [1, 2, 3, 4, 5]
for isi in x:
    if isi == 15:
        break
    print(isi)

for isi in x:
    print(isi)
    if isi == 7:
        break

for isi in x:
    if isi == 5:
        continue
    print(isi)

for isi in buah:
    for j in x:
        print(isi)
        print(j)


kata = "Coba deh a"
