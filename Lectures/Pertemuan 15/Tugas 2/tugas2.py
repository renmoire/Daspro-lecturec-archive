
#? Nama: Irenia Maisa Kamila
#? NIM: 2506031
#? Kelas: 1B

import pandas as x

st = x.read_csv("Data_Dummy.csv")

st["Tanggal"] = x.to_datetime(st["Tanggal"])
st["Bulan"] = st["Tanggal"].dt.month

#Nomoer 1
incomebulanan = st.groupby("Bulan")["Total"].sum()
print(incomebulanan)

#Nomor 2
avg = st["Total"].mean()
print(avg)

#Nomor 3
incomemin = st["Total"].min()
incomemax = st["Total"].max()
print(f"Pendapatan paling sedikit: {incomemin}")
print(f"Pendapatan paling banyak: {incomemax}")

#Nomor 4
terlaris = st.groupby("Produk")["Jumlah"].sum().sort_values(ascending=False)
print(terlaris)