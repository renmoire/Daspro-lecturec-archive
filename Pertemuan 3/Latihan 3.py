# Nama: Irenia Maisa Kamila
# NIM: 2506031
# Kelas: 1B

while True:
    listnama = input("=======================================\nInput 10 nama dan pisahkan dengan spasi: ").split()
    if len(listnama)==10:
        break
    else:
        print("Jumlah tidak sesuai, harus 10. Silakan coba ulang.")

print("=======================================\nList nama yang telah di-input:")
print(listnama)
print(f"=======================================\nJumlah nama yang di-list: {len(listnama)}")