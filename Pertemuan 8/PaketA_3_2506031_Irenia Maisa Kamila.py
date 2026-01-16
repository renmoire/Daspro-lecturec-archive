
#! Nama: Irenia Maisa Kamila
#! NIM: 2506031
#! Kelas: 1B
#! Paket soal: A

genap = 0
ganjil = 0

while True:
    lembur = int(input("Input lembur: "))

    if lembur < 0:
        print(f"Total jam lembur pada tanggal genap: {genap}")
        print(f"Total jam lembur pada tanggal ganjil: {ganjil}")
        break
    if lembur % 2 == 0:
        genap = genap + lembur
    elif lembur % 2 != 0:
        ganjil = ganjil + lembur