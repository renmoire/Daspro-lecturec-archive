    
#! Nama: Irenia Maisa Kamila
#! NIM: 2506031
#! Kelas: 1B

data = []

def stokbarang(barang):
    return int(barang['stok'])

def shellsort(listdata):
    n = len(listdata)
    gap = n // 2

    while gap > 0:
        for item in range(gap, n):
            sementara = listdata[item]
            jarak = item

            while jarak >= gap and int(listdata[jarak - gap]['stok']) > int(sementara['stok']):
                listdata[jarak] = listdata[jarak - gap]
                jarak -= gap

            listdata[jarak] = sementara

        gap //= 2
    return listdata

def pendataanbarang(jumlah):
    jumlahjenisbarang = jumlah
    for item in range(jumlahjenisbarang):
        print(f"\nData barang ke-{item + 1}")
        nama = input("Nama: ")
        kode = input("Kode: ")
        stok = input("Stok: ")
        data.append({
            "nama": nama,
            "kode": kode,
            "stok": stok
        })
    if len(data):
        print("Data berhasil diinput")

def output(data):
    if not data:
        print(f"{"-"*30}\nBelum ada data barang\n")
        return
    print(f"{"-"*30}\nDaftar barang di gudang:\n")
    for item, barang in enumerate(data):
        barang = data[item]
        print(f"{item+1}. Kode: {barang['kode']}\nNama: {barang['nama']}\nStok: {barang['stok']}\n")

def mengurutkan():
    if not data:
        print(f"{"-"*30}\nBelum ada data barang untuk diurutkan\n")
        return
    shellsort(data)
    output(data)

def search(mencari):
    if not data:
        print(f"{"-"*30}\nTidak ada data barang yang dicari\n")
        return
    barangditemukan = None
    for item in data:
        if item['nama'].lower() == mencari.lower():
            barangditemukan = item
            break
        if barangditemukan:
            print(f"Barang ditemukan: Kode {barangditemukan['kode']}, nama {barangditemukan['nama']}, stok {barangditemukan['stok']}")
        else:
            print("Maaf, barang tidak ada pada inventori kami")

def kritis(minstok):
    if not data:
        print(f"{"-"*30}\nBelum ada barang untuk membuat laporan\n")
        return
    
    barangkritis = []

    for item in data:
        if int(item['stok']) < minstok:
            print(f"Kode: {item['kode']}, nama: {item['nama']}, stok: {item['stok']}")
            barangkritis.append(item)
        
        total = len(barangkritis)

        if total == 0 :
            print("Tidak ada barang dengan stok di bawah batas minimum")
            print(F"Jumlah barang kritis: 0")
        else:
            print(f"Jumlah barang kritis: {total}")


while True:
    print("Silakan pilih opsi berikut:\n\n1. Menginput barang\n2. Cek barang\n3. Cek barang yang telah diurut\n4. Mencari barang\n5. Stok Kritis\n6. Selesai")
    pilih = input("Silakan pilih (1-6): ")

    if pilih == "1":
        jumlahbarang = input("Masukan jumlah jenis barang: ")
        if jumlahbarang.isdigit():
            jumlahbarangangka = int(jumlahbarang)
            if jumlahbarangangka > 0:
                pendataanbarang(jumlahbarangangka)
            else:
                print("Jumlah barang harus lebih dari 0")
        else:
            print("Hanya angka yang valid untuk jumlah barang")
    elif pilih == "2":
        output(data)
    elif pilih == "3":
        mengurutkan()
    elif pilih == "4":
        cari = input("Nama barang: ")
        search(cari)
    elif pilih == "5":
        mins = input("Masukan batas minimun stok:")

        if mins.isdigit():
            minstok = int(mins)
            if minstok >= 0:
                kritis(minstok)
            else:
                print("Batas minimum stok tidak boleh negatif")
        else:
            print("Hanya angka yang valid untuk batas stok")
    elif pilih == "6":
        print("Program selesai")
        break
    else:
        print("Hanya bisa memilih 1-6")