
#! Nama: Irenia Maisa Kamila
#! NIM: 2506031
#! Kelas: 1B

inputan = input("Berapa banyak calon peminjam yang akan diinput? ")
datapeminjam = {}

if inputan >= "0" and inputan <= "9":
    inputan = int(inputan)

    for isi in range(1, inputan + 1):
        print(f"\nMenginput data calon peminjam ke-{isi}")
        print("Silakan isi data berikut.\n")
        nama = input("Nama: ")

        gaji = []
        for isi in range(1, 4):
            nominal = int(input(f"Gaji bulan ke-{isi} untuk {nama}: "))
            gaji.append(nominal)
        datapeminjam[nama] = {"Gaji": gaji}

    for kiri, kanan in datapeminjam.items():
        gaji = kanan["Gaji"]
        avg = sum(gaji) / 3
        avg = float(avg)
        selisih = max(gaji) - min(gaji)

        if avg > 5000000 and selisih <= 2500000:
            keputusan = "Disetujui penuh."
        elif avg > 3000000 and selisih <= 1500000:
            keputusan = "Disetujui parsial."
        else:
            keputusan = "Ditolak."

    datapeminjam[nama]["Rata-rata"] = avg
    datapeminjam[nama]["Selisih"] = selisih
    datapeminjam[nama]["Status"] = keputusan

    for nama, data in datapeminjam.items():
        print(f"\nNama: {nama.capitalize()}")
        print(f"- Rata-rata Gaji: Rp{round(avg, 3)}")
        print(f"- Selisih Gaji: Rp{selisih}")
        print(f"- Status: {keputusan}")

else:
    print("Tidak valid. Hanya bisa menginput angka.")