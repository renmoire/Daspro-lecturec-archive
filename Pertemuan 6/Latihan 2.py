
# ! Nama: Irenia Maissa Kamila
# ! NIM: 2506031
# ! Kelas: 1B

bilangan = int(input("Coba masukkan nilai: "))
if bilangan % 2 == 0:
    if bilangan > 0:
        print(f"Bilangan {bilangan} adalah genap positif")
    if bilangan < 0:
        print(f"Bilangan {bilangan} adalah genap negatif")
else:
    if bilangan > 0:
        print(f"Bilangan {bilangan} adalah ganjil positif")
    if bilangan < 0:
        print(f"Bilangan {bilangan} adalah ganjil negatif")