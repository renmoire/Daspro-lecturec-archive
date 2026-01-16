
#! Latihan UTS #1

#? Latihan percobaan login

# kesempatan = 3

# while kesempatan > 0:
#     username = input("Nama pengguna: ")
#     sandi = input("Sandi: ")
#     if username == "Twist" and sandi == "Korn":
#         print(f"Selamat datang {username}. Login telah berhasil")
#         break
#     elif username != "Twist" and sandi != "Korn":
#         kesempatan = kesempatan - 1
#         print(f"Data yang anda masukan salah. Sisa kesempatan: {kesempatan}")
#         if kesempatan == 0:
#             print("Anda tidak bisa melanjuti tindakan ini lagi.")
#             break
#         continue



#? Latihan

genap = 0
ganjil = 0

while True:
    penjualan = int(input("Input penjualan: "))

    if penjualan < 0:
        print(f"Total penjualan pada tanggal genap: {genap}")
        print(f"Total penjualan pada tanggal ganjil: {ganjil}")
        break

    elif penjualan % 2 == 0:
        genap = genap + penjualan
    elif penjualan % 2 != 0:
        ganjil = ganjil + penjualan



# #? Latihan ketiga

data = 0
total = 0
peringatan = 0

while True:
    transaksi = int(input("Input jumlah transaksi: "))
    
    if data == 0:
        data = transaksi
        
    if transaksi < data:
        peringatan += 1
        
    elif transaksi > data:
        total += transaksi
        peringatan = 0

    else:
        peringatan = 0

    data = transaksi
    
    if peringatan == 3:
        break

if total < 30:
    print(f"Total transaksi yang meningkat {total}")
    total = "Kurang"
    print(f"Kategori: {total}")
elif total >= 30 and total <= 80:
    print(f"Total transaksi yang meningkat {total}")
    total = "Cukup"
    print(f"Kategori: {total}")
elif total > 80:
    print(f"Total transaksi yang meningkat {total}")
    total = "Baik"
    print(f"Kategori: {total}")




#? Latihan lanjutan

datakaryawan = {}
karyawan = input("Masukan jumlah karyawan yang akan didata: ")

if karyawan >= "0" and  karyawan <= "9":
    karyawan = int(karyawan)

    print("-"*50)
    print(f"Silakan menginput {karyawan} data karyawan dengan mengisi data berikut")
    for isi in range(1, karyawan + 1):
        print(f"\nData karyawan ke-{isi}")
        nama = input("Nama: ")
        gaji = int(input("Gaji: "))
        datakaryawan[nama] = gaji
    
    total = sum(datakaryawan.values())
    avg = total / karyawan
    avg = float(avg)
    kdgt = max(datakaryawan.values()) # karyawan dengan gaji tertinggi
    if gaji == kdgt:
        kdgt = nama

    print("-"*50)
    print("Laporan gaji")
    print(f"- Total gaji seluruh karyawan: Rp{total}")
    print(f"- Rata-rata  gaji karyawan: Rp{avg}")
    print(f"- Karyawan dengan gaji tertinggi: {kdgt}")