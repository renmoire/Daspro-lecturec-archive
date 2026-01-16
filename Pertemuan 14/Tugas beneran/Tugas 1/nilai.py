
#? Nama: Irenia Maisa Kamila
#? NIM: 2506031
#? Kelas: 1B

totalnilai = 0
totalsiswa = 0

print(f"{"-"*7} Data Siswa {"-"*7}")
with open("nilai_siswa.txt", "r") as file:
    for item in file:
        item = item.strip()
        nama, nilai = item.split(":")
        nilai = int(nilai)
        totalsiswa += 1
        totalnilai += nilai
        print(item)
        
avg = totalnilai / totalsiswa

print(f"\nJumlah siswa: {totalsiswa}\nTotal nilai: {totalnilai}\nRata-rata: {avg}\n{"-"*25}")