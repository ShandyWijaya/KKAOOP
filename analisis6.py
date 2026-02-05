from abc import ABC, abstractmethod

class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar):
        self.nama = nama
        self.__stok = 0
        self.__harga_dasar = harga_dasar


    def get_stok(self):
        return self.__stok


    def _get_harga_dasar(self):
        return self.__harga_dasar


    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {jumlah} unit.")

    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass


class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, processor):
        super().__init__(nama, harga_dasar)
        self.processor = processor

    def tampilkan_detail(self):
        harga = self._get_harga_dasar()
        pajak = harga * 0.10
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")
        print(f" Harga Dasar: Rp {harga:,} | Pajak(10%): Rp {int(pajak):,}")

    def hitung_harga_total(self, jumlah):
        harga = self._get_harga_dasar()
        pajak = harga * 0.10
        total = (harga + pajak) * jumlah
        return total


class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, kamera):
        super().__init__(nama, harga_dasar)
        self.kamera = kamera

    def tampilkan_detail(self):
        harga = self._get_harga_dasar()
        pajak = harga * 0.05
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        print(f" Harga Dasar: Rp {harga:,} | Pajak(5%): Rp {int(pajak):,}")

    def hitung_harga_total(self, jumlah):
        harga = self._get_harga_dasar()
        pajak = harga * 0.05
        total = (harga + pajak) * jumlah
        return total


def proses_transaksi(daftar_barang):
    print("\n--- STRUK TRANSAKSI ---")
    total_belanja = 0
    nomor = 1

    for barang, jumlah in daftar_barang:
        barang.tampilkan_detail()
        subtotal = barang.hitung_harga_total(jumlah)
        print(f" Beli: {jumlah} unit | Subtotal: Rp {int(subtotal):,}")
        print()
        total_belanja += subtotal
        nomor += 1

    print("----------------------------------------")
    print(f"TOTAL TAGIHAN: Rp {int(total_belanja):,}")
    print("----------------------------------------")


print("--- SETUP DATA ---")

laptop1 = Laptop("ROG Zephyrus", 20000000, "Ryzen 9")
hp1 = Smartphone("iPhone 13", 15000000, "12MP")

laptop1.tambah_stok(10)
hp1.tambah_stok(-5)   # gagal
hp1.tambah_stok(20)

# User beli barang
keranjang = [
    (laptop1, 2),
    (hp1, 1)
]

proses_transaksi(keranjang)