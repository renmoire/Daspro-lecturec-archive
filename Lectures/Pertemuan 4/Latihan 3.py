# Nama: Irenia Maisa Kamila
# NIM: 2506031
# Kelas: 1B

student_info = {
    "Alice": {"age": 20, "major": "Computer Science"},
    "Bob": {"age": 21, "major": "Mathematics"},
    "Charlie": {"age": 19, "major": "Physics"}
}


while True:
    nama = input("Nama: ")

    if nama in student_info:
        age = student_info[nama]["age"]
        major = student_info[nama]["major"]
        print(f"Umur {nama} tuh {age}, prodinya {major}")
        break
    else:
        print("Nama tidak valid. Silakan pulang")