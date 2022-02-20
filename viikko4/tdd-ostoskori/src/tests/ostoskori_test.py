import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 3)
        self.kurkku = Tuote("Kurkku", 10)

    # step 1
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
    
    
    # step 2
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    
    # step 3
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(), 3)
    
    # step 4
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_2_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.kurkku)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    # step 5
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteiden_hintojen_summa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.kurkku)
        self.assertEqual(self.kori.hinta(), 13)

    # step 6
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_2_tavaraa(self):
        self.kori.lisaa_tuote(self.kurkku)
        self.kori.lisaa_tuote(self.kurkku)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    # step 7
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_2_kertaa_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.kurkku)
        self.kori.lisaa_tuote(self.kurkku)
        # self.assertEqual(self.kori.hinta(), 20)
        self.assertEqual(self.kori.hinta(), 2 * self.kurkku.hinta())
    
    # step 8
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)
    
    # step 
    # step 
    # step 
    # step 
    # step 
    # step 
    # step 