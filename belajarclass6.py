class Kendaraan:
    def berjalan(self):
        print('berjalan...')

class Mobil(Kendaraan):
    def berjalan(self, kecepatan, satuan = " km/j"):
        super().berjalan()
        print(f"berjalan dengan kecepatan {kecepatan}{satuan}")
    pass

sepeda = Kendaraan()
sedan = Mobil()

sepeda.berjalan()
sedan.berjalan(150)