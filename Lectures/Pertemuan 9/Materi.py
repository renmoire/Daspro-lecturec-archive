
#? Nama: Irenia Maisa Kamila
#? NIM: 2506031
#? Kelas: 1B

ini_global = 1 #ini variabel global

def penjumlahan(a, b):
    hasil = a + b
    return hasil #? variabel lokal karena di dalam fungsi

print(penjumlahan(2, 3))

def greeting(nama):
    print(f"Halo, {nama}!")

greeting("Ren")





#! menyampurkan variabel global dan lokal, maka hasilnya akan seperti ini
hasil = 1 
def penjumlahan(a, b):
    hasil = a + b
    print(hasil) #? variabel ini akan tertimpa di fungsi
    return hasil

print(penjumlahan(2, 3))
print(hasil)





globalvar = 10

def globalfunction():
    print(f"Nilai lobal variabel adalah {globalvar}")

globalfunction()
print(globalvar)
globalfunction()


def lokalfunction():
    lokalvar = 5
    print(f"Nilai dari lokal variabel adalah {lokalvar}")

lokalfunction()
# print(lokalvar) #? error karena mengambil variabel di dalam fungsi, tidak di identasi yang sama




#! Arguments
def pengurangan(a, b):
    print(a - b)

pengurangan(5, 2)
pengurangan(2, 5)
pengurangan(b=2, a=5)

#? parameter adalah variabel di dalam fungsi, dalam case ini
#? nama = "Jane Doe" adalah parameter
def greeting(nama = "Jane Doe"):
    print(f"Halo, {nama}!")

greeting()
greeting("Ren")





#! Arbitrary Argument
def angakterakhir(*angka):
    print(f"Angka terakhir yang dimasukan adalah {angka[-1]}")

angakterakhir(1,2,8,9,4,5,9)
angakterakhir((1,2,8,9,4,5,9)) #? bisa mengubah menjadi tipe data lain, tambah kurung


#? jika ingin mendefinisikan tipe data di parameternya apa
def pengurangan(a: int, b: int):
    print(a - b)


#! Arbitary Keyword Arguments menggunakan **
#! Parameternya jadi dictionary
def cekangkatiga(**angka):
    print(f"Angka ketiga yaitu {angka['ketiga']}")

cekangkatiga(pertama = 1, kedua = 2, ketiga = 3, keempat = 4)
cekangkatiga(pertama = 1, kedua = 2, ketiga = 5, keempat = 4, kelima = 3)



def namabuah(buah):
    for item in buah:
        print(item)

namabuah(["Mangga", "Apel", "Jeruk"])


#! Pass

def tambah():
    pass

def kurang():
    pass

def kosong():
    pass










#? LATIHAN KEDUA
# def login():
#     print("Silakan untuk mengisi informasi login.")
#     username = "Daspro2023"
#     sandi = "Latihan"

#     kesempatan = 3

#     while kesempatan > 0:
#         nama = input("Nama Pengguna: ")
#         sandii = input("Sandi: ")

#         if sandii != "Latihan":
#             kesempatan -= 1
#             print(f"Login salah! tersisa {kesempatan} kesempatan.")
#         else:
#             print("Login berhasil.")
#             break

#     print("Akun terkunci.")

# login()