from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class PeliTehdas:
    def anna_peli(self, vastaus):
        if vastaus not in ['a', 'b', 'c']:
            return None

        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

        if vastaus == 'a':
            return self._pvp()
        elif vastaus == 'b':
            return self._pvAi()
        elif vastaus == 'c':
            return self._pvBetterAi()

    def _pvp(self):
        return KPSPelaajaVsPelaaja()

    def _pvAi(self):
        return KPSTekoaly()

    def _pvBetterAi(self):
        return KPSParempiTekoaly()
