import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_korti_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(2500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 35.0)
    
    def test_kortille_ei_voi_ladata_neg_rahaa(self):
        self.maksukortti.lataa_rahaa(-2500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_ota_rahaa_ei_vie_saldoa_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(-2500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
    
    def test_ota_rahaa_vahentaa_saldoa_oikein(self):
        self.maksukortti.ota_rahaa(250)

        self.assertEqual(self.maksukortti.saldo_euroina(), 7.50)
    
    def test_ota_rahaa_palautttaa_True_jos_rahat_riittavat(self):

        self.assertEqual(self.maksukortti.ota_rahaa(250), True)
    
    def test_ota_rahaa_palautttaa_False_jos_rahat_ei_riita(self):

        self.assertEqual(self.maksukortti.ota_rahaa(10000), False)
    
    def test_ota_rahaa_palautttaa_None_maara_nega(self):

        self.assertEqual(self.maksukortti.ota_rahaa(-1), None)