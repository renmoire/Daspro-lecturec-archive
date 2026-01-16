# Nama: Irenia Maisa Kamila
# NIM: 2506031
# Kelas: 1B
# Paket soal 1C



#izin menambahkan penjelasan singkat

tinggi = 400 #cm
panjang = 8 #m
lebar = 1000 #cm

panjang1 = panjang * 100 #mengonversikan panjang dari meter ke cm


luaspermukaan = 2 * (panjang1 * tinggi) + 2 * (lebar * tinggi)
print(f"Luas permukaan: {luaspermukaan} cm^2")

cmkemeter = luaspermukaan / 100 #mengubah cm ke meter
print(f"Jika dikonversikan menjadi meter: {int(cmkemeter)}")

biaya = 450000 * cmkemeter #per m^2
print(f"Jumlah biaya yang harus dikeluarkan adalah Rp.{int(biaya)},00")