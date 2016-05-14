import word_wrap
import unittest

class WordWrapTest(unittest.TestCase):
    
    def test_paragraph(self):
        columns = 10
        paragraph = "123 4567\t 89\n\
                    abcdefghijklmnopqrst uvwxyz\n\
                    1234567 89ABCDEFG"
        output = "123 4567\n"
        output += "89 abcdef-\n"
        output += "ghijklmno-\n"
        output += "pqrst\n"
        output += "uvwxyz\n"
        output += "1234567\n"
        output += "89ABCDEFG"
        para = word_wrap.WordWrap(paragraph, columns)
        self.assertEqual(output, para.wrapped)
    
    def test_word_split(self):
        columns = 10
        long_string = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        word = word_wrap.WordWrap(long_string, columns)
        output = "123456789-\nABCDEFGHI-\nJKLMNOPQR-\nSTUVWXYZ"
        self.assertEqual(word.wrapped, output)