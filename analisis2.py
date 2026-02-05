class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")


class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)
        self.mana = mana

    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")

    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)
        else:
            print(f"{self.name} gagal skill! Mana tidak cukup.")


class Assassin(Hero):
    def __init__(self, name, hp, attack_power, critical_chance):
        super().__init__(name, hp, attack_power)
        self.critical_chance = critical_chance

    def info(self):
        print(f"{self.name} [Assassin] | HP: {self.hp} | Critical Chance: {self.critical_chance}%")

    def skill_shadow_strike(self, lawan):
        print(f"{self.name} menggunakan Shadow Strike ke {lawan.name}!")
        damage = self.attack_power * 3
        lawan.diserang(damage)


print("\n--- Update Class Hero ---")

eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)
hayabusa = Assassin("Hayabusa", 90, 25, 50)

eudora.info()
hayabusa.info()

print("\n--- Pertarungan Dimulai ---")
eudora.serang(balmond)
eudora.skill_fireball(balmond)

hayabusa.serang(balmond)
hayabusa.skill_shadow_strike(balmond)