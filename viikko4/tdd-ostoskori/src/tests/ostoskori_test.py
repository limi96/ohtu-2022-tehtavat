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
        # testaa etta metodin palauttaman listan pituus 1
 
    # step 9
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostos = self.kori.ostokset()[0]
 
        # testaa taalla, etta palautetun listan ensimmainen ostos on halutunkaltainen.
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    # step 10
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.kurkku)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)

    # step 11
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_yhden_ostoksen(self):
        self.kori.lisaa_tuote(self.kurkku)
        self.kori.lisaa_tuote(self.kurkku)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    # step 12 
    def test_Kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_ostoksen_jolla_sama_nimi_kuin_tuotteella_ja_lukumaara_2(self):
        self.kori.lisaa_tuote(self.kurkku)
        self.kori.lisaa_tuote(self.kurkku)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Kurkku")
        self.assertEqual(ostos.lukumaara(), 2)

    # step 13
    def test_Jos_korissa_on_kaksi_samaa_tuotetta_ja_toinen_naista_poistetaan_jaa_koriin_ostos_jossa_on_tuotetta_1_kpl(self):
        self.kori.lisaa_tuote(self.kurkku)
        self.kori.lisaa_tuote(self.kurkku)
        self.kori.poista_tuote(self.kurkku)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Kurkku")
        self.assertEqual(ostos.lukumaara(), 1)

    # step 14
    def test_Jos_koriin_on_lisatty_tuote_ja_sama_tuote_poistetaan_on_kori_taman_jalkeen_tyhja(self):
        self.kori.lisaa_tuote(self.kurkku)
        self.kori.poista_tuote(self.kurkku)

        ostokset = self.kori.ostokset()

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(ostokset), 0)

    # step 15
    def test_Metodi_tyhjenna_tyhjentaa_korin(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.kurkku)

        self.kori.tyhjenna()

        ostokset = self.kori.ostokset()

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(ostokset), 0)
