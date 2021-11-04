import statistics
import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player('Semenko', 'EDM', 4, 12),
            Player('Lemieux', 'PIT', 45, 54),
            Player('Kurri', 'EDM', 37, 53),
            Player('Yzerman', 'DET', 42, 56),
            Player('Gretzky', 'EDM', 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    def testKonstruktoriLuoListanJossaKurri(self):
        kurri = self.statistics.search('Kurri')

        self.assertAlmostEqual(kurri.name, 'Kurri')

    def testListassaEiSelannetta(self):
        selanne = self.statistics.search('Selänne')

        self.assertIsNone(selanne)

    def testTeamPalauttaaOikeanKokoisenJoukkueen(self):
        joukkue = self.statistics.team('DET')

        self.assertAlmostEqual(len(joukkue), 1)

    def testTeamPalauttaaOikeanSisallon(self):
        joukkue = self.statistics.team('EDM')
        edm = [
            Player('Semenko', 'EDM', 4, 12),
            Player('Kurri', 'EDM', 37, 53),
            Player('Gretzky', 'EDM', 35, 89)
        ]

        self.assertListEqual([p.name for p in joukkue], [pl.name for pl in edm])

    def testTopScorerIsRightOne(self):
        top = self.statistics.top_scorers(1)
        self.assertAlmostEqual(top[0].name, 'Gretzky')
