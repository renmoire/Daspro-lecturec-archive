
#? Nama: Irenia Maisa Kamila
#? NIM: 2506031
#? Kelas: 1B

import pandas as x

#Nomor 2
st = x.read_csv('Daftar_Mahasiswa_2018.csv')
print(st.head(10))

#Nomor 3
sorted = st.sort_values(by="Nama")
print(sorted.head(10))

#Nomor 4
dipilih = sorted[[
    "NIM",
    "Nama",
    "L/P",
    "Status",
    "SKS",
    "IPK",
    "Lama Studi(Smt)"
]]

#Nomor 5
avg = st["IPK"].mean()
print(f"Rata-rata IPK: {avg}")

#Nomor 6
men = (st["L/P"] == "L").sum()
women = (st["L/P"] == "P").sum()
print(f"Jumlah laki-laki: {men}")
print(f"Jumlah perempuan: {women}")

#Nomor 7
womenty = st[(st["L/P"] == "P") & (st["Status"] == "Terdaftar")]
print(womenty)

#Nomor 8
noregist = st[st["Status"] != "Terdaftar"]
print(noregist)