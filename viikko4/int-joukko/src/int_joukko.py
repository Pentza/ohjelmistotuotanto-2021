class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):

        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise ValueError("Kapasiteetin ja kasvatuskoon täytyy olla positiivinen kokonaisluku")

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti

        self.indeksi = 0

    def kuuluu(self, n):
        return n in self.lukujono

    def lisaa(self, n):
        if self.indeksi == len(self.lukujono):
            self.lukujono += [0] * self.kasvatuskoko

        if n not in self.lukujono:
            self.lukujono[self.indeksi] = n
            self.indeksi = self.indeksi + 1
            return True
        return False

    def poista(self, n):
        if n in self.lukujono:
            self.lukujono.remove(n)
            self.indeksi -= 1
            self.lukujono += [0]
            return True
        return False

    def mahtavuus(self):
        return self.indeksi

    def to_int_list(self):
        return [x for x in self.lukujono if x != 0]

    @staticmethod
    def yhdiste(a, b):
        tulosjoukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for alkio in a_taulu:
            tulosjoukko.lisaa(alkio)
        for alkio in b_taulu:
            tulosjoukko.lisaa(alkio)

        return tulosjoukko

    @staticmethod
    def leikkaus(a, b):
        tulosjoukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for alkio in list(set(a_taulu).intersection(b_taulu)):
            tulosjoukko.lisaa(alkio)
        
        return tulosjoukko

    @staticmethod
    def erotus(a, b):
        tulosjoukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for alkio in a_taulu:
            tulosjoukko.lisaa(alkio)

        for alkio in b_taulu:
            tulosjoukko.poista(alkio)

        return tulosjoukko

    def __str__(self):
        tuloste = ', '.join([str(x) for x in self.lukujono if x != 0])

        return f'{{{tuloste}}}'
        