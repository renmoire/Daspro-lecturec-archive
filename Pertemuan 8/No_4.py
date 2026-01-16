
#! Nama: Irenia Maisa Kamila
#! NIM: 2506031
#! Kelas: 1B
#! Paket soal: A

datakaryawan = {}
karyawan = input("Masukan jumlah karyawan yang akan didata: ")

if karyawan >= "0" and  karyawan <= "9":
    karyawan = int(karyawan)

    for isi in range(1, karyawan + 1):
        print(f"\nInput data untuk karyawan ke-{isi}")
        nama = input("Nama: ")
        gaji = int(input("Gaji: "))
        datakaryawan[nama] = gaji
        
    totalgaji = sum(datakaryawan.values())
    avg = totalgaji / karyawan
    avg = round(float(avg), 2)
    tertinggi = max(datakaryawan.values())
    if gaji == tertinggi:
        tertinggi = nama

print("Laporan gaji")
print(f"- Total gaji seluruh karyawan: Rp{totalgaji}")
print(f"- Rata-rata  gaji karyawan: Rp{avg}")
print(f"- Karyawan dengan gaji tertinggi: {tertinggi}")