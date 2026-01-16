# # ? Konversi menit ke detik and vice versa

# introduksi = "Selamat datang di kalkulator konversi menit ke detik (and vice versa)"
# print("="*90)
# print(introduksi)


# while True:
#     while True:
#         print("=" * 90)
#         print("Menu Konversi:")
#         print("1. Menit ke detik\n2. Detik ke Menit\n3. Selesaikan program")
#         pilihan = int(input("Silakan pilih (1-3): "))

#         if pilihan < 1 or pilihan > 3:
#             print("Hanya bisa memilih 1-3. Silakang ulangi kembali.")
#         else:
#             break

#     if pilihan == 1:
#         isi = int(input("── Menit yang ingin dijadikan detik: "))
#         tambahdetik = (input("── Tambahan detik (jika ada): "))
#         add = int(tambahdetik) if tambahdetik.strip() != "" else 0
#         mkd = int(isi * 60) + add
#         if add > 0:
#             print(f"\n   Hasil konversi:\n   {isi} menit {add} detik = {mkd} detik")
#             lanjut = input("\nLanjutkan kalkulator (ya/tidak)? ")
#             if lanjut.lower() == "ya":
#                 continue
#             if lanjut.lower() == "tidak":
#                 print("Terima kasih telah menggunakan kalkulator ini.")
#                 print("="*90)
#                 break
#         else:
#             print(f"\n   Hasil konversi:\n   {isi} menit = {mkd} detik")
#             lanjut = input("\nLanjutkan kalkulator (ya/tidak)? ")
#             if lanjut.lower() == "ya":
#                 continue
#             if lanjut.lower() == "tidak":
#                 print("Terima kasih telah menggunakan kalkulator ini.")
#                 print("="*90)
#                 break

#     if pilihan == 2:
#         isi = int(input("── Detik yang ingin dijadikan menit: "))
#         dkm = round(float(isi / 60), 1)
#         print(f"\n   Hasil konversi:\n   {isi} detik = {dkm} menit")
#         lanjut = input("\nLanjutkan kalkulator (ya/tidak)? ")
#         if lanjut.lower() == "ya":
#                 continue
#         if lanjut.lower() == "tidak":
#                 print("Terima kasih telah menggunakan kalkulator ini.")
#                 print("="*90)
#                 break
    
#     if pilihan == 3:
#         print("Program selesai. Terima kasih telah menggunakan kalkulator konversi ini.")
#         print("="*90)
#         break








# # ? Menghitung luas permukaan

# # ! soal no 1
# sisi = 7
# print(f"DIketahui sebuah kubus mempunyai sisi {sisi}.")

# luaspermukaan = 6 * sisi**2
# print(f"Maka luas permukaan kubus tersebut adalah {luaspermukaan} cm^2")


# # ! soal no 2
# panjang = 10
# lebar = 6
# tinggi = 4
# print(f"Diketahui sebuah balok memiliki panjang {panjang} cm, lebar {lebar} cm, tinggi {tinggi} cm.")

# pt = panjang * tinggi
# pl = panjang * lebar
# lt = lebar * tinggi
# luaspermukaan = 2 * (pl + pt + lt)
# print(f"Maka luas permukaan balok tersebut adalah {luaspermukaan} cm^2")


# # ! soal no 3
# import math
# r = 7 #cm
# tinggi = 10 #cm
# print(f"Diketahui sebuah tabung:\nJari-jari {r} cm\nTinggi {tinggi} cm")

# luaspermukaan = 2 * math.pi * r * (r +  tinggi)
# print(f"\nMaka luas permukaan tabung tersebut adalah {round(luaspermukaan, 2)} cm^2")


# # ! soal no 4
# import math
# r =  14 #cm
# print(f"Diketahui sebuah bola basket memiliki jari-jari {r} cm")

# luaspermukaan = 4 * math.pi * r**2
# print(f'Maka luas permukaan bola tersebut adalah {round(luaspermukaan, 2)} cm^2')


# # ! soal no 5
# import math
# r = 7 #cm
# tinggi = 24 #cm
# print(f"Diketahui sebuah kerucung\nJari-jari: {r} cm\nTinggi: {tinggi} cm")


# s = math.sqrt(r**2 + tinggi**2)
# luaspermukaan = math.pi * r * (r + s)
# print(f"Maka luas permukaan kerucut tersebut adalah {round(luaspermukaan)} cm^2")


# # ? latihan import math
# import math
# test = math.sqrt(64)
# test2 = math.pow(5, 2)
# test3 = math.factorial(3)
# print(f"{round(test)}, {int(test2)}, {test3}")









# # ? latihan list, tuple, set
# #menambahkan input user ke index yang dipilih user
# nama = ["Andi", "Budi", "Citra", "Kurniawan", "Wawan"]
# print(nama)
# tambahanuser = input("Input nama: ")
# index = int(input("Mau ditaro di mana? "))

# nama[index-1] = tambahanuser
# print(nama)






# # * MEMASUKAN BERBAGAI TIPE DATA KE TIPE DATA LAINNYA
# abwa = [("Mangga", "Jeruk"), {"manggis", "anggur", "ceri"}]
# waba = (["istimewa", "ingin"], {"manggsisisi"})

# print(abwa)
# print(type(abwa[0]))
# print(type(abwa[1]))

# print(waba)
# print(type(waba[0]))
# print(type(waba[1]))







# #for loop print
# angka = [2, 4, 6, 8, 10]
# for x in angka:
#     print(x)




# nilai = [70, 90, 87, 67, 67, 99, 92, 94]
# print(nilai)
# inputan = int(input("Nilai mana: "))
# print("Nilai yang kamu pilih adalah: ", nilai[inputan-1])



# ? latihan dict

# bvc = ["mangga", "jeruk", "buah", "makanan", "jaksa", "kurnia", "manggiz"]

# for x in bvc:
#     print(x)


# for b in range(3):
#     print(b)

# ayu = {
#     "Nama": "Ayu",
#     "Umur": "19"
# }
# for k, l in ayu.items():
#     print(k, ":", l)

# for y in ayu:
#     print(y)






















# # ? latihan dict #2
# keranjang = {}
# item = ["Kangkung", "Mangga", "Tomat", "Pakcoy", "Blueberry"]

# for x in item:
#     value = input(f"Masukan {x}: ")
#     if x == "Mangga":
#         value = int(value)
#     keranjang[x] = value
# print(keranjang)


# # ? latihan dict #3
# nilaimahasiswa = {}
# matkul = ["LTIK", "PRPL", "Daspro", "Matdas", "PBI"]

# for item in matkul:
#     nilaiinput = int(input(f"Input nilai {item}: "))
#     nilaimahasiswa[item] = nilaiinput

# # print(nilaimahasiswa)                   # * cara mainstream untuk print dictionary

# for x, y in nilaimahasiswa.items():     # * cara gg buat print dictionary kayak pro
#     print(f"{x}: {y}")







# # ? latihan dict #3 INI GG BANGET

# kucing = {
#     "Nama": "",
#     "Ras": "",
#     "Warna": ""
# }

# kucingya = {}

# print("Selamat datang di CATTOOO")

# while True:
#     print("="*50)
#     print("Menu: \n1. Kucing yang ada\n2. Nambah kucing\n3. Selesaikan program")
#     inputanuser = int(input("Silakan pilih menu (1-3): "))

#     if inputanuser < 1 or inputanuser > 3:
#         print("\n!!! Kami hanya memiliki 3 menu. Silakan ulangi kembali !!!")
#         continue

#     if inputanuser == 1:
#         if not kucingya:
#             print("Belum memiliki kucing")
#         else:
#             for kiri, kanan in kucingya.items():
#                 print(f"{kiri}: {kanan}")

#     if inputanuser == 2:
#         for kiri, kanan in kucing.items():
#             coba = input(f"{kiri} yang anda mau: ")
#             kucingya[kiri] = coba
#             print("Berhasil menginput!")
#             ingin = input("Ingin lihat kucingnya? (ya/tidak): ")
#             if ingin.lower() == "ya":
#                 continue
#             else:
#                 break



#         # print("="*50)
#         # print("Spesifikasi kucing: ")
      


# # ? latihan dict #4
# kucingb = {}
# kucingl = {
#     "Nama": "John",
#     "Warna": "Abu",
#     "Ras": "Persia"
# }

# print("-"*50)
# print("Kucing yang kamu miliki:")
# for kiri, kanan in kucingl.items():
#     print(f"- {kiri}: {kanan}")

# tanya = input("Apakah ingin mengganti kucing baru? (ya/tidak): ")
# if tanya == "ya":
#     print("Silakan input data ini:")
#     for kiri, kanan in kucingl.items():
#         inputanuser = input(f"{kiri}: ")
#         kucingb[kiri] = inputanuser

# print("-"*50)
# print("Kucing baru kamu:")
# for kiri, kanan in kucingb.items():
#     print(f"- {kiri}: {kanan}")

# if tanya == "tidak":
#     print("Program akan ditutup, terima kasih telah menggunakan.")







# # ! menghitung jarak lari work by adi
# p = 80 * 100
# l = 3200

# L = 7 * 2 *(p + l)/100000
# print("Total jarak yang ditempuh oleh Bu Rinda adalah :", L, "km")