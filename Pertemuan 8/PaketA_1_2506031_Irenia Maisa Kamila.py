
#! Nama: Irenia Maisa Kamila
#! NIM: 2506031
#! Kelas: 1B
#! Paket soal: A

kesempatan = 3

print("Silakan input informasi akun untuk login!")
while kesempatan > 0:
    username = input("Nama pengguna: ")
    sandi = input("Sandi: ")

    if username == "Techno".capitalize() and sandi == "works123".lower():
        print("Login berhasil! Selamat datang di sistem TechnoWorks!")
        break
    else:
        kesempatan -= 1
        print(f"Login salah! Kesempatan tersisa {kesempatan} kali lagi")
        if kesempatan == 0:
            print("Akses ditolak. Anda telah gagal login 3 kali. Silakan hubungi Kepala HRD untuk mereset password")