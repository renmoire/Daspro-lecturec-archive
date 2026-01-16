
#! Nama: Irenia Maisa Kamila
#! NIM: 2506031
#! Kelas: 1B


#? LATIHAN 1
z = int(input("Masukan jumlah angka Fibonacci: "))
def fibonacci(z):
    x, y = 0, 1
    hasil = []

    for isi in range(z):
        hasil.append(x)
        x, y = y, x + y
    return hasil

print(fibonacci(z))







#? LATIHAN 2
print("Silakan masukan data berikut dalam bentuk sentimeter")
r = int(input("Jari-jari: "))
t = int(input("Tinggi tabung: "))

def voltab(r, t):
    vol = 3.14 * r**2 * t
    return vol

print(f"Volume tabung adalah {round(voltab(r, t))} cm^3")







#? LATIHAN 3
def nilai(*angka):
    total = sum(angka)
    avg = total / len(angka)
    return total, avg

anu = []

print("Silakan masukan nilai negatif untuk berhenti.")
while True:
    a = int(input("Nilai: "))
    if a < 0:
        break
    anu.append(a)

total, avg = nilai(*anu)
print(f"Total nilai: {total}")
print(f"Rata-rata: {round(avg, 2)}")