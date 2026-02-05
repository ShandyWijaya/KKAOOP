class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

hero1 = Hero("Layla", 100, 20)

# Mengubah nilai hp hero1
hero1.hp = 500

print(hero1.hp)

class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    # Method menyerang
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    # Method diserang
    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")

hero1 = Hero("Layla", 100, 20)
hero2 = Hero("Zilong", 120, 15)

print("\n--- Pertarungan Dimulai ---")

hero1.serang(hero2)  # Layla menyerang Zilong
hero2.serang(hero1)  # Zilong membalas