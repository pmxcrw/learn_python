import zeckendorf
import unittest

class ZekTest(unittest.TestCase):
    
    def test_init(self):
        zek = zeckendorf.Zeckendorf()
        self.assertEqual([1, 2], zek.fibs)
        
    def test_update_fibs(self):
        zek = zeckendorf.Zeckendorf()
        zek.update_fibs(30)
        self.assertEqual([1, 2, 3, 5, 8, 13, 21], zek.fibs)
    
    def test_eleven(self):
        zek = zeckendorf.Zeckendorf()
        self.assertEqual(10100, zek.single_zek(11))
    
    def test_table_20(self):
        zek = zeckendorf.Zeckendorf()
        output = {2: 10,
                  3: 100,
                  4: 101,
                  5: 1000,
                  6: 1001,
                  7: 1010,
                  8: 10000,
                  9: 10001,
                  10: 10010,
                  11: 10100,
                  12: 10101,
                  13: 100000,
                  14: 100001,
                  15: 100010,
                  16: 100100,
                  17: 100101,
                  18: 101000,
                  19: 101001,
                  20: 101010}
        output_string = "1:\t1"
        for i, z in output.items():
            output_string += "\n{}:\t{}".format(i, z)
        self.assertEqual(output_string, zek.zek_table(20))
        