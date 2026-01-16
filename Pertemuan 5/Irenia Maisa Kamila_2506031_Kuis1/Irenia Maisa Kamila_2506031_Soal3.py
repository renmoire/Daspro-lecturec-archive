# Nama: Irenia Maisa Kamila
# NIM: 2506031
# Kelas: 1B
# Paket soal 1C


print("-"*90)
print("Diketahui mobil balap melaju 1 putaran selama 11 menit 30 detik, maka:")
menit = 11
detik = 30

mkd = menit * 60
print(f"Hasil konversi {menit} menit {detik} detik adalah \n{mkd} detik")



print("-"*90)
print("Program untuk mengonversi")
menit = int(input("Masukan menit yang ingin diubah ke detik: "))
detik = int(input("Tambahan detik (kalau ada (input 0 jika tidak)): "))

mkd = (menit * 60) + detik

print(f"Hasil konversi:\n{menit} menit {detik} detik = {mkd} detik")