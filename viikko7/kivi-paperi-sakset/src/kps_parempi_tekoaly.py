from kps import KPS
from tekoaly_parannettu import TekoalyParannettu

class KPSParempiTekoaly(KPS):
    def __init__(self, muisti=10) -> None:
        super().__init__()
        self._ai = TekoalyParannettu(muisti)

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._ai.anna_siirto()
        self._ai.aseta_siirto(tokan_siirto)
        return tokan_siirto
