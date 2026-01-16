
# ! Nama: Irenia Maissa Kamila
# ! NIM: 2506031
# ! Kelas: 1B

print("="*30)
print("Silakan input data berikut")

bb = input("Berat Badan: ") #kg
tinggi = input("Tinggi: ") #cm

if (bb >= "0" and bb <= "9") and (tinggi >= "0" and tinggi <= "9"):
    bb = int(bb)
    tinggi = int(tinggi)

    tinggi1 = float(tinggi / 100)  #ubah cm ke m
    bmi = float(bb / tinggi**2)

    if bmi < 18.5:
        kategori = "ceking"
    elif bmi >= 18.5 and bmi < 25:
        kategori = "normal"
    elif bmi >= 25 and bmi < 30:
        kategori = "berlebihan"
    elif bmi >= 30:
        kategori = "obesitas"
    print("="*30)
    print(f"BMI yang diinput adalah {round(bmi, 2)}, termasuk ke dalam kategori {kategori}")
else: 
    print("Gak valid, kudu angka")