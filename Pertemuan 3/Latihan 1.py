# Nama: Irenia Maisa Kamila
# NIM: 2506031
# Kelas: 1B

z = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
z[2] = "cherry"

nambah = input("==========================\nTambahkan item: ")
terserah = int(input("==========================\nMau ditaro di urutan ke berapa? "))

z.insert(terserah, nambah)
print(z)

print("\nBerikut list setelah disesuaikan dengan abjad")
z.sort()
print(z)