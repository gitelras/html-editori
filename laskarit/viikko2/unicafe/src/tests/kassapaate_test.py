import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_alussa_on_oikea_maara_rahaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_alussa_on_oikea_maara_edullisia(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_alussa_on_oikea_maara_maukkaita(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_syo_edullisesti_kateisalla_kasvattaa_lounaiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_syo_edullisesti_kateisalla_antaa_vaihtorahat(self):
        vaihtorahat = self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(vaihtorahat, 10)
    
    def test_syo_edullisesti_palauttaa_rahat_jos_ei_varaa(self):
        vaihtorahat = self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(vaihtorahat, 230)
    
    def test_syo_edullisesti_kateisalla_ei_kasvata_lounaiden_maaraa_jos_ei_varaa(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_syo_maukkaasti_kateisalla_kasvattaa_lounaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(410)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_syo_maukkaasti_kateisalla_antaa_vaihtorahat(self):
        vaihtorahat = self.kassapaate.syo_maukkaasti_kateisella(410)
        self.assertEqual(vaihtorahat, 10)
    
    def test_syo_maukkaasti_palauttaa_rahat_jos_ei_varaa(self):
        vaihtorahat = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(vaihtorahat, 300)
    
    def test_syo_maukkaasti_kateisalla_ei_kasvata_lounaiden_maaraa_jos_ei_varaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_syo_edullisesti_kortilla_veloitetaan(self):
        osto = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(osto, True)
    
    def test_syo_edullisesti_kortilla_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_syo_edullisesti_kortilla_ei_veloiteta_jos_ei_varaa(self):
        self.maksukortti = Maksukortti(200)
        osto = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(osto, False)
    
    def test_syo_edullisesti_kortilla_lounaiden_maara_ei_kasva_jos_ei_varaa(self):
        self.maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_syo_maukkaasti_kortilla_veloitetaan(self):
        osto = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(osto, True)
    
    def test_syo_maukkaasti_kortilla_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_syo_maukkaasti_kortilla_ei_veloiteta_jos_ei_varaa(self):
        self.maksukortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 300)
    
    def test_syo_maukkaasti_kortilla_lounaiden_maara_ei_kasva_jos_ei_varaa(self):
        self.maksukortti = Maksukortti(300)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_osto_kortilla_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_lataa_rahaa_kortille_kasvattaa_rahamaaraa_kassassa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)
    
    def test_lataa_rahaa_kortille_muuttaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        saldo = self.maksukortti.saldo
        self.assertEqual(saldo, 1500)
    
    def test_negatiivista_rahaa_ei_ladata_kortille(self):
        lataa = self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-100)
        self.assertEqual(lataa, None)

    def test_kassassa_rahaa_euroina_toimii(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
