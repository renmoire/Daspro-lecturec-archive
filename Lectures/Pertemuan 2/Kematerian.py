print("Hello, World!")
print(1+5)
# ini adalah komentar
"""ini
adalah
komentar"""


# PELAJARI KONSEP STRING, INTEGER & FLOAT!!




# Variable
x = "Aku"
n = "mau"
m = "makan."
print(x, n, m)

a = int(3)
b = float(3)
c = str(3)
print(a, b, c)

f, g, h = "Strawberry, ","mangga, ", "apel."
print(f, g, h)

e = t = r = "Buah"
print(e, t, r)





# Quiz 2
o = 2
i = 6
print(str(o + i) + "5" * 4)




# Lanjut
q = 11
w = 21
print("Aku nomor", q)
print("Nomorku adalah {0} dan dia adalah {1}".format(q, w))
print(f"Nomorku adalah {q} dan nomornya adalah {w}")





# String
print(len(x))

l = """I'm the bone of my sword."""
print(l)

# Slicing String
print(l[:7])
print(l[8:])
print(l[0:13])

# Modifikasi String
print(l.upper())
print(l.lower())

mn = " Hello, World! "
print(mn.strip())

mm = "Hello, World!"
print(mm.replace("o", "u"))
print(mm.split(","))

teks = "Hello, welcome \"Ren\" from Minang Bogor"
print(teks)

teks2 = "Hello, \nWelcome Ren from Minang Bogor"
print(teks2)





# Identasi
"""
Tingkat 1
    Tingkat 2
        Tingkat 3
"""





# Input
nama = input("Masukan nama Anda: ")
print(f"Selamat datang, {nama}")

umur = input("Masukan umur Anda: ")
print(f"Umur anda: {umur}")
print(type(umur))

umur = int(input("Masukan umur Anda: "))
print(f"Umur anda: {umur}")
print(type(umur))





# Tipe Data
print(type(nama))
print(type(umur))
