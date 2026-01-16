
#! Nama: Irenia Maisa Kamila
#! NIM: 2506031
#! Kelas: 1B

user = input("Masukan angka: ")

if user >= "0" and user <= "9":
    user = int(user)

    print("-"*20)
    print(f"Tabel perkalian {user}")
    print("-"*20)
    for isi in range(1, 11):
        print(f"{isi} x {user} = {user * isi}")

else:
    print("Tidak valid. Hanya bisa menginput angka dan harus angka positif.")