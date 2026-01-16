# Nama: Irenia Maisa Kamila
# NIM: 2506031
# Kelas: 1B

students = {
    "Alice": "Computer Science",
    "Bob": "Mathematics",
    "Charlie": "Physics",
    "David": "Computer Science",
    "Eva": "Mathematics"
}

major = set(students.values())

# major = prodi
# jumlahmajor = ada berapa orang di prodi tsb

prodi = set(students.values())
jumlahprodi = {}

for prodi in prodi:
    count = len([a for a in students.values() if a == prodi])
    jumlahprodi[prodi] = count

for major, count in jumlahprodi.items():
    print(f"Major {major} ada {count} orang")
print()