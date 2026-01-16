
#! Nama: Irenia Maisa Kamila
#! NIM: 2506031
#! Kelas: 1B

def ngitung(jam1, menit1, detik1, jam2, menit2, detik2):
    detik = detik2 - detik1
    menit = menit2 - menit1
    jam = jam2 - jam1

    if detik < 0:
        detik += 60
        menit -= 1
    if menit < 0:
        menit += 60
        jam -= 1
    if jam < 0:
        jam += 24

    return jam, menit, detik


jam1 = int(input("Jam mulai: "))
menit1 = int(input("Menit mulai: "))
detik1 = int(input("Detik mulai: "))

jam2 = int(input("Jam selesai: "))
menit2 = int(input("Menit selesai: "))
detik2 = int(input("Detik selesai: "))

jam, menit, detik = ngitung(jam1, menit1, detik1, jam2, menit2, detik2)
print(f"Lama lari: {jam} jam - {menit} menit - {detik} detik")
