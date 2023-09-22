#in adalah modifier yang bisa diakses oleh publik
class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi
    
segitigaku = Segitiga(100,80)

# print(f"alas : {segitigaku.alas}")
# print(f"tinggi : {segitigaku.tinggi}")
# print(f"luas : {segitigaku.luas}")

#ini adalah protected modifier
class Mobil:
   def __init__(self, merk):
       #menginisialisasi modifier protected dengan menambahkan garis bawah
       #setelah self.
       self._merk = merk 

class MobilBalap(Mobil):
    def __init__(self, merk, total_gear):
        super().__init__(merk)
        self.total_gear = total_gear
    def pamer(self):
        #akses _merk dari subclass
        print(f'ini mobil {self._merk} dengan total gear {self.total_gear}')
    

# sedan = Mobil("Toyota")
# print(f'merk: {sedan._merk}')
# ferrari = MobilBalap('Ferrari', 8)
# ferrari.pamer()

#ini adalah private modifier
#ini hanya bisa diakse didalam class saja
class Motor:
    def __init__(self,merk):
        self.__merk = merk

    def tampilkan_merek(self):
        print(f'Merk: {self.__merk}')
honda = Motor('honda')
honda.tampilkan_merek()