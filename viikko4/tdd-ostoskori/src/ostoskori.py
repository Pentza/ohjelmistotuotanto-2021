from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.__ostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return sum([o.lukumaara() for o in self.__ostokset])
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        summa = 0
        for ostos in self.__ostokset:
            summa += ostos.hinta()

        return summa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        ostos = Ostos(lisattava)
        tuote = self.hae_tuote(lisattava)
        if not tuote:
            self.__ostokset.append(ostos)
        else:
            tuote.muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        tuote = self.hae_tuote(poistettava)
        if not tuote:
            return 

        tuote.muuta_lukumaaraa(-1)
        if tuote.lukumaara() == 0:
            self.__ostokset.remove(tuote)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.__ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on

    def hae_tuote(self, tuote: Tuote):
        ostos = Ostos(tuote)
        for o in self.__ostokset:
            if o.tuotteen_nimi() == ostos.tuotteen_nimi():
                return o
        return None

