class Kucing:
    def __init__(self, warna,usia):
        self.warna = warna
        self.usia = usia

class mahasiswa:
    def __init__(self,nama, asal, kucing):
        self.kucing = kucing
        self.nama = nama
        self.asal = asal

    def perkenalan(self):
        print(f'perkenalkan nama saya {self.nama}, saya berasal dari {self.asal}')
        print(f'saya memiliki kucing berwarna {self.kucing.warna}, ')