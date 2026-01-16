
# ! Nama: Irenia Maissa Kamila
# ! NIM: 2506031
# ! Kelas: 1B

print("Alat prediksi kategori model catwalk")
gender = int(input("Jenis kelamin:\n- 1. Wanita\n- 2. Pria\nSilakan pilih 1-2: "))

gagal = []

if gender == 1:
    print("Gender adalah wanita.")
    umur = int(input("Masukan umur: "))
    tinggi = int(input("Tinggi badan: "))
    iq = int(input("IQnya: "))
    if umur >= 18 and umur <= 25:
        if tinggi == 170:
            if iq >= 130:
                print("Bisatuh bang jadi model")
            else:
                print("Gagal bisa jadi model, tidak memenuhi kategori sebagai model.")
        else:
            print("Gagal bisa jadi model, tidak memenuhi kategori sebagai model.")
    else:
        print("Gagal bisa jadi model, tidak memenuhi kategori sebagai model.")

if gender == 2:
    print("Gender adalah pria.")
    umur = int(input("Masukan umur: "))
    tinggi = int(input("Tinggi badan: "))
    iq = int(input("IQnya: "))
    if umur >= 18 and umur <= 25:
        if tinggi == 175:
            if iq >= 130:
                print("Bisatuh bang jadi model")
            else:
                print("Gagal bisa jadi model, tidak memenuhi kategori sebagai model.")
        else:
            print("Gagal bisa jadi model, tidak memenuhi kategori sebagai model.")
    else:
        print("Gagal bisa jadi model, tidak memenuhi kategori sebagai model.")
pass