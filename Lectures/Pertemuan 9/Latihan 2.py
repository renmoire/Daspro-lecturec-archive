
#! Nama: Irenia Maisa Kamila
#! NIM: 2506031
#! Kelas: 1B

def login():
    for kesempatan in range(3):
        if input("Nama Pengguna: ") != "Daspro2023":
            print("Akun tidak ditemukan")
            return
        
        if input("Sandi: ") == "Latihan":
            print("Login berhasil!")
            return
        print(f"Login salah! tersisa {2 - kesempatan} kesempatan")
    print("Akun terkunci.")

login()
