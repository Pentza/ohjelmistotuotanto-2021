from kps import KPS
from tekoaly import Tekoaly

class KPSTekoaly(KPS):
    def __init__(self) -> None:
        self._ai = Tekoaly()
    
    def _toisen_siirto(self, ensimmaisen_siirto):
        toisen_siirto = self._ai.anna_siirto()

        return toisen_siirto
