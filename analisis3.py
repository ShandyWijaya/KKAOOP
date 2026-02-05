class Hero:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        # HP private (tidak bisa diakses langsung dari luar class)
        self.__hp = hp_awal

    # GETTER: untuk melihat HP
    def get_hp(self):
        return self.__hp

    # SETTER: untuk mengubah HP dengan aturan
    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    def diserang(self, damage):
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")


# -- Uji Coba --
hero1 = Hero("Layla", 100)

# hero1.__hp = 9999  # GAGAL (tidak mengubah hp asli)
# print(hero1.__hp)  # ERROR

hero1.set_hp(-50)  # coba set negatif
print(hero1.get_hp())  # Output: 0