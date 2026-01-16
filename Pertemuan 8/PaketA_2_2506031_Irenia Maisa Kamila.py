
#! Nama: Irenia Maisa Kamila
#! NIM: 2506031
#! Kelas: 1B
#! Paket soal: A

sementara = 0
total = 0
peringatan = 0

while True:
    tugas = int(input("Input jumlah tugas: "))
    if sementara == 0:
        sementara = tugas
    if tugas < sementara:
        peringatan += 1
    elif tugas > sementara:
        total += tugas
        peringatan = 0

    else:
        peringatan = 0

    sementara = tugas

    if peringatan == 3:
        break

if total < 30:
    kategori = "Kurang"
if total >= 30 and total <= 80:
    kategori = "Cukup"
if total > 80:
    kategori = "Baik"

print(f"Total tugas yang meningkat: {total}")
print(f"Kategori: {kategori}")