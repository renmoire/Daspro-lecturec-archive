# Nama: Irenia Maisa Kamila
# NIM: 2506031
# Kelas: 1B

print("Selamat datang di kalkulator konversi suhu!\nSilakan input suhu celcius di bawah ini.")
celcius = int(input("Input suhu dalam Celcius: "))
reamur = float(celcius*4/5)
fahrenheit = float((celcius*9/5)+32)
kelvin = float(celcius+273)
print(f"Hasil konversi suhu {celcius}°C (Celcius) ke skala suhu lainnya adalah:\n= {reamur}°R (Reamur)\n= {fahrenheit}°F (Fahrenheit)\n= {kelvin} K (Kelvin)")