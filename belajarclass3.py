class kucing:
    warna = None
    usia = None

class mahasiswa:
    nama = None
    asal = None

    def perkenalan(self):
        print(f"Perkenalkan nama saya {self.nama}, dan berasal dari {self.asal}")
kucing1 = kucing()
kucing1.warna= 'hitam'
kucing1.usia= '5 bulan'

nijika = mahasiswa()
nijika.nama = "Nijika Ijichi"
nijika.asal = "Fukuoka"
nijika.perkenalan()
