import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            return [5, 10, 15, 20, 0][tuote_id]

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            return [
                Tuote(0, "kahvi", 3), 
                Tuote(1, "maito", 5), 
                Tuote(2, "leipä", 2),
                Tuote(3, "juusto", 4),
                Tuote(4, "olut", 1)
                ][tuote_id]

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        # palautetaan aina arvo 40
        self.viitegeneraattori_mock.uusi.return_value = 40

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla argumenteilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 40, "12345", "33333-44455", 5)

    def test_usean_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "54321")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "54321", "33333-44455", 7)

    def test_kaksi_samaa_tuotetta_joita_varastossa_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "54321")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "54321", "33333-44455", 10)

    def test_tuote_jota_varastossa_ja_tuote_jota_ei_varastossa_tilisiirto(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)
        self.kauppa.lisaa_koriin(4)
        self.kauppa.tilimaksu("pekka", "54321")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "54321", "33333-44455", 4)




        



