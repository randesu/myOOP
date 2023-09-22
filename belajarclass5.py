class Orang:
    #Merupakan class induk
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal

    def perkenalan(self):
        print(f"Perkenalkan nama saya adalah {self.nama}, dan saya berasal dari {self.asal}")

class Pelajar(Orang):
    #Merupakan child atau turunan dari class orang sebagai induk 
    def __init__(self, nama, asal, sekolah):
        super().__init__(nama, asal)
        #menambahkan Atribut khusus pelajar
        self.sekolah = sekolah
    
    pass

class Pekerja(Orang):
    #merupakan child atau turunan dari class orang sebagai induk
    def __init__(self, nama, asal,tempat_kerja):
        Orang.__init__(self,nama,asal)
        self.tempat_kerja = tempat_kerja
    pass

Yohan = Orang('Yohan', 'Malang')
Yohan.perkenalan()


budi = Pelajar('Budi','jepara','SMA 1 Jayakarta')
budi.perkenalan()
print(f"Saya bersekolah di {budi.sekolah}")

yoman = Pekerja('yoman','madiun','Samator Gas')
yoman.perkenalan()
print(f"Saya bekerja di perusahaan {yoman.tempat_kerja}")
