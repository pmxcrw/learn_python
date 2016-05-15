import unsplice
import unittest

class UnspliceTest(unittest.TestCase):
    
    def test_unchanged(self):
        input = "abcdef"
        output = input
        word = unsplice.Unsplice(input)
        self.assertEqual(output, word.unsplice())
        
    def test_only_newline(self):
        input = "abc\ndef"
        output = input
        word = unsplice.Unsplice(input)
        self.assertEqual(output, word.unsplice())       

    def test_only_backslah(self):
        input = "abc\\def"
        output = input
        word = unsplice.Unsplice(input)
        self.assertEqual(output, word.unsplice())
    
    def test_wrong_order(self):
        input = "abc\n\\def"
        output = input
        word = unsplice.Unsplice(input)
        self.assertEqual(output, word.unsplice())
    
    def test_one_strip(self):
        input = "abc\\\ndef"
        output = "abcdef"
        word = unsplice.Unsplice(input)
        self.assertEqual(output, word.unsplice())
        
    def test_two_strip(self):
        input = "ab\\\ncd\\\nef"
        output = "abcdef"
        word = unsplice.Unsplice(input)
        self.assertEqual(output, word.unsplice())