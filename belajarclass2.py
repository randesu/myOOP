class segitiga():
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    
    def get_luas(self):
        return 0.5 * self.alas * self.tinggi
    
    @staticmethod
    def get_abc():
        return "abcd"
    
segitiga1 = segitiga(1,2)
print(segitiga1.get_luas())
print(segitiga.get_abc())