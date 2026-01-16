
# Nama: Irenia Maisa Kamila
# NIMI: 2506031
# Kelas: 1B

data = []

def shellsort(listdata):
    jumlah = len(listdata)
    gap = jumlah // 2

    while gap > 0:
        for item in range(gap, jumlah):
            sementara = listdata[item]
            n = item

            while n >= gap and int(listdata[n - gap]['stok']) > int(sementara['stok']):
                listdata[n] = listdata[n - gap]
                n -= gap

                listdata[n] = sementara
            
        gap //= 2
    return listdata
    
# Nomor 1, pendataan/penginputan barang
def pendataanbarang(jumlah):
    jenisbarang = jumlah
    for item in range (jenisbarang):
        print(f"\nData barang ke-{item+1}")
        nama = input("Nama: ")
        kode = input("Kode: ")
        stok = input("Stok: ")
        
        data.append({
            "nama": nama,
            "kode": kode,
            "stok": stok
        })
    if len(data):
        print("Data berhasil disimpan")

# Nomor 2, memeriksa barang di gudang
def memeriksagudang(data):
    if not data:
        print(f"{"-"*30}\nTidak ada barang dalam gudang")
        return
    print(f"{"-"*30}\nDaftar barang di gudang:")
    for item, barang in enumerate(data):
        barang = data[item]
        print(f"{item+1}. Nama: {barang['nama']}, kode: {barang['kode']}, stok: {barang['stok']}")
    
# Nomor 3, mengurutkan, saya menggunakan shell short karena mendapatkan jenis sort tersebut saat penugasan kemarin
def urutan():
    if not data:
        print(f"{"-"*30}\nTidak ada yang bisa diurut")
        return
    shellsort(data)
    memeriksagudang(data)
    return

# Nomor 4, mencari barang dengan nama
def mencari(cari):
    if not data:
        print(f"{"-"*30}\nTidak ada barang yang bisa dicari")
        return
    barangditemukan = None
    for item in data:
        if item['nama'].lower() == cari.lower():
            barangditemukan = item
            break
    if barangditemukan:
        print(f"Barang ditemukan: Kode {barangditemukan['kode']}, Nama {barangditemukan['nama']}, stok {barangditemukan['stok']}")
    else:
        print("Maaf, Barang tidak ada pada inventory kami")

# Nomor 5, laporan barang yang stoknya menipis
def menipis(krisisstok):
    if not data:
        print(f"{"-"*30}\nTidak ada yang bisa dijadikan laporan")

    yangmenipis = []
    print(f"Laporan stok barang yang menipis di bawah {krisisstok}")

    for item in data:
        if int(item['stok']) < krisisstok:
            print(f"Kode: {item['kode']}, nama: {item['nama']}, stok: {item['stok']}")
            yangmenipis.append(item)

    total = len(yangmenipis)

    if total == 0:
        print(f"{"-"*30}\nTidak ada barang dengan stok di bawah batas minimum")
        print("Jumlah barang kritis: 0")
    else:
        print(f"Jumlah barang kritis: {total}")

# Menjalankan program
while True:
    print(f"\nSilakan pilih menu (1-6):\n1. Menginput barang\n2. Cek barang\n3. Barang yang telah diurutkan\n4. Mencari barang\n5. Laporan stok menipis\n6. Selesai")
    inputan = input("-> ")

    if inputan == "1":
        jumlahbarang = input("Masukan jumlah jenis barang: ")
        if jumlahbarang.isdigit():
            jumlahbarang = int(jumlahbarang)
            if jumlahbarang > 0:
                pendataanbarang(jumlahbarang)
            else:
                print("Jumlah barang harus lebih dari 0")
        else:
            print("Jumlah barang harus berupa angka")

    elif inputan == "2":
        memeriksagudang(data)

    elif inputan == "3":
        urutan()

    elif inputan == "4":
        barangyangdicari = input("Nama barang: ")
        mencari(barangyangdicari)
    
    elif inputan == "5":
        stokminus = input("Masukan batas minimun stok: ")
        if stokminus.isdigit():
            mins = int(stokminus)
            if mins >= 0:
                menipis(mins)
            else:
                print("Batas minimun stok tidak boleh negatif")
        else:
            print("Hanya angka yang valid untuk inputan")
    
    elif inputan == "6":
        print("Program selesai")
        break
    
    else:
        print("Hanya bisa memilih 1-6")