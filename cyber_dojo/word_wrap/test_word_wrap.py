import word_wrap
import unittest

class WordWrapTest(unittest.TestCase):
    
    def test_paragraph(self):
        columns = 10
        paragraph = "123 4567 89nabcdefghijklmnopqrst uvwxyz12345\
                    123456789A 89ABCDEFGHIJK"
        output = "123 4567\n"
        output += "89 abcdef-\n"
        output += "ghijklmno-\n"
        output += "pqrst uvw-\n"
        output += "xyz12345\n"
        output += "123456789A\n"
        output += "89ABCDEFG-\n"
        output += "HIJK"
        para = word_wrap.WordWrap(paragraph, columns)
        self.assertEqual(output, para.wrap())
    
    def test_long_word_split(self):
        columns = 10
        long_string = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        word = word_wrap.WordWrap(long_string, columns)
        output = "123456789-\nABCDEFGHI-\nJKLMNOPQR-\nSTUVWXYZ"
        self.assertEqual(word.wrap(), output)