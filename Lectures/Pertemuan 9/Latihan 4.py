
#! Nama: Irenia Maisa Kamila
#! NIM: 2506031
#! Kelas: 1B

def penjualan():
    jumlahproduk = int(input("Berapa banyak produk yang terjual hari ini? "))
    gaji = []

    for isi in range(1, jumlahproduk + 1):
        while True:
            harga = input(f"Masukan harga produk ke-{isi}: ")

            if harga.isdigit():
                harga = int(harga)
                if harga > 0:
                    gaji.append(harga)
                    break
                else:
                    print("Input harus berupa ANGKA POSITIF!")
            else:
                print("Input harus berupa ANGKA!")

    total = sum(gaji)
    avg = total / jumlahproduk
    avg = float(avg)
    
    print(f"Total pendapatan: Rp{total}")
    print(f"Rata-rata pendapatan: Rp{round(avg, 2)}")

penjualan()