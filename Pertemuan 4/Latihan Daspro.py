a = {"apel", "jeruk", "ceri", "durian"}
b = {"apel", "jeruk", "ceri", "durian", "apel", "manggis", "beruang"}
c = {"zebra"}
f = {"jagung"}
# print(a)
# print(b)
# print("Jumlah set A:", len(a))

# a.add("bangmomakan")
# b.update(c)
# a.update(b)
# print(a)

# print(c.union(f)) #menambahkan set ke set yang baru dengan union
# v = a.union(b)
# print(v)

a.intersection_update(b) #menggabungkan item yang sama
print(a)

a.intersection(b) #hanya menampilkan item yang sama
print("Intersection/Kesamaan:", a)

# v = a.symmetric_difference(b) #hanya menampilkan item yang berbeda
# print("Difference/Perbedaan: ", v)

# a.pop() #menghapus item dari set
# print("Pop/Hapus 1 item random: ", a)

# a.clear() #menghapus keseluruhan item dari set
# print(a)



# # menambahkan list ke set
# k = {"apel", "jeruk", "ceri", "durian"}
# j = ["apel", "jeruk", "ceri", "durian", "apel", "manggis", "beruang"]
# k.update(j)
# print(k)
# print(type(k))

# # menambahkan tuple ke set
# o = {"apel", "jeruk", "ceri", "durian"}
# l = ("apel", "jeruk", "ceri", "durian", "apel", "manggis", "beruang", "makanbangbang")
# o.update(l)
# print(o)
# print(type(o))



# abc = {"apel", "jeruk", "ceri", "durian", 20, 10.6, True} 
# #bisa terdiri dari tipe data yang berbeda
# print(abc)



# for jumlahitem in a:
#     if "jeruk" in jumlahitem:
#         print(jumlahitem)



# print("apel" in a)
# print("mangga" in b)
















# # Dictionary
# owang = {
#     "Nama: ": "Ilham",
#     "Usia: ": 19,
#     "Hobi: ": ["Workout", "Mengrajin"],
#     "Jantan: ": True
# }
# print(owang)
# print(len(owang))

# # mengakses item di dict
# print(owang["Nama: "])
# print(owang.get("Usia: "))

# # mengakses keys
# print(owang.keys())
# print(type(owang.keys()))

# # mengakses values
# print(owang.values())

# # menambahkan
# owang["Nama: "] = "Adit" #mengganti
# print(owang)

# owang["Detak jantung: "] = 79
# print(owang)

# owang.update({"Baju: ": "Hitam"})
# print(owang)

# x = owang.items()
# print(x)

# if "Nama: " in owang:
#     print("ada key 'nama' di owang")

# # menghapus item di dit
# owang.pop("Hobi: ")
# print(owang)


# # buah = dict(
# #     nama = "apel",
# #     warna = "merah",
# #     manis = True
# # )
# # print(buah)
