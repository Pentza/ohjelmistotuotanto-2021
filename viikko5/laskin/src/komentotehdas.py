class Komento:
    def __init__(self, sovellus, io):
        self.sovellus = sovellus
        self.io = io
        self.edellinen = sovellus.tulos

    def lue(self):
        arvo = 0
        try:
            arvo = int(self.io())
        except:
            pass
        return arvo
    
    def kumoa(self):
        self.sovellus.aseta_arvo(self.edellinen)

class Summa(Komento):
    def suorita(self):
        self.edellinen = self.sovellus.tulos
        self.sovellus.plus(self.lue())

class Erotus(Komento):
    def suorita(self):
        self.edellinen = self.sovellus.tulos
        self.sovellus.miinus(self.lue())

class Nollaa(Komento):
    def suorita(self):
        self.edellinen = self.sovellus.tulos
        self.sovellus.nollaa()

class Kumoa(Komento):
    def suorita(self):
        self.edellinen = self.sovellus.tulos