import zekendorf
import unittest

class ZekTest(unittest.TestCase):
    
    def test_init(self):
        zek = zekendorf.Zekendorf()
        self.assertEqual([1, 2], zek.fibs)
        
    def test_update_fibs(self):
        zek = zekendorf.Zekendorf()
        zek.update_fibs(20)
        self.assertEqual([1, 2, 3, 5, 8, 13], zek.fibs)
    
    def test_eleven(self):
        zek = zekendorf.Zekendorf()
        self.assertEqual(10100, zek.single_zek(11))
        