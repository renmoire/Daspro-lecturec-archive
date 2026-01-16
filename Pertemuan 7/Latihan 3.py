
#! Nama: Irenia Maisa Kamila
#! NIM: 2506031
#! Kelas: 1B

inventory = [
    {"nama": "Pedang Besi", "tipe": "Weapon", "rarity": "Common"},
    {"nama": "Health Potion", "tipe": "Consumable", "rarity": "Common"},
    {"nama": "Panah Api", "tipe": "Weapon", "rarity": "Rare"},
    {"nama": "Jubah Gaib", "tipe": "Armor", "rarity": "Rare"},
    {"nama": "Excalibur", "tipe": "Weapon", "rarity": "Epic"}
]

while True:
    inputan = input("Pilih rarity untuk difilter (Common, Rare, Epic): ")
    ygvalid = ["Common", "Rare", "Epic"]
    if inputan.capitalize() not in ygvalid:
        print("\nTidak ada dalam daftar 'rarity'. Silakan ulangi.")
        continue
    else:
        break

print(f"Item dengan rarity '{inputan}':")
for isi in inventory:
    if isi["rarity"].lower() == inputan.lower():
        print(f"- {isi['nama']}")