class Komento:
    def __init__(self, sovellus, io):
        self.sovellus = sovellus
        self.io = io

    def lue(self):
        arvo = 0
        try:
            arvo = int(self.io())
        except:
            pass
        return arvo

class Summa(Komento):
    def suorita(self):
        self.sovellus.plus(self.lue())
        

class Erotus(Komento):
    def suorita(self):
        self.sovellus.miinus(self.lue())

class Nollaa(Komento):
    def suorita(self):
        self.sovellus.nollaa()

class Kumoa(Komento):
    def suorita(self):
        pass