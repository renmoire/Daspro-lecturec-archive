# Nama: Irenia Maisa Kamila
# NIM: 2506031
# Kelas: 1B

a = ["apellele", "jeruk", "ceri", "durian", "mangga", "beruang", "naga"]
b = ["huahuhuha", "roti"]

print(len(a))
print(a[5])
print(a[1:6])
a.append("sirsak") #menambah item
a[2] = "manggis" #mergganti
a.insert(0, "jangkar") #menambah
a.pop(3) #menghapus
print(a)

a.extend(b) #menggabungkan variabel
print(a)

a.sort() #mengurutkan berdasarkan abjadnya
print(a)

z = ["apellele", "jeruk", "ceri", "durian", "mangga", "beruang", "naga", 20, True, 10.2]
print(z)
#variable ga melulu string









n = ("apel", "jeruk", "ceri", "durian", "apel")

print(len(n))
print(n[3])
print(n[1:3])

l = list(n) #mengubah tuple n menjadi list l
l[3] = "semangka" #mengubah list index 3 menjasi semangka
n = tuple(l) #mengubah list l menjadi tuple n kembali
print(n)

n = ("apel","jeruk", "ceri", "durian", "apel", False, 0.2, 9) #tuple juga bisa menggunankan tipe data lain

buah = ("ayam bakar", "mau makan", "tinggal makan")
(a, b, c) = buah
print(a)
print(b)
print(c)