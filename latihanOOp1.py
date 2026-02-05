class AkunBank:
 def __init__(self, saldo):
  self.__saldo = saldo # Private attribute
 def cek_saldo(self):
  return self.__saldo
 def setor(self, jumlah):
  if jumlah > 0:
   self.__saldo += jumlah
rekening = AkunBank(1000)
rekening.setor(500)
print(rekening.cek_saldo()) # Output: 1500
# print(rekening.__saldo) # Ini akan Error! Tidak bisa akses
langsung