import yatzy
import unittest


class TestYatzy(unittest.TestCase):
    
    def test_simple(self):
        '''simple example test'''
        dice = yatzy.Yatzy(roll=[5,6,5,5,2], category="fives")
        self.assertEqual(15, dice.score())
        
    def test_chance(self):
        '''chance should give sum of each dice'''
        dice = yatzy.Yatzy(roll=[1,2,3,4,5], category="chance")
        self.assertEqual(15, dice.score())

    def test_yatzee_true(self):
        '''yatzy scores 50 if all numbers same'''
        dice = yatzy.Yatzy(roll=[1,1,1,1,1], category="yatzy")
        self.assertEqual(50, dice.score())
    
    def test_yatzee_false(self):
        '''yatzy scores zero if numbers are different'''
        dice = yatzy.Yatzy(roll=[1,2,3,4,5], category="yatzy")
        self.assertEqual(0, dice.score())

    def test_singles_true(self):
        '''yatzy scores sum of given number'''
        dice = yatzy.Yatzy(roll=[1,2,1,2,3], category="twos")
        self.assertEqual(4, dice.score())
    
    def test_singles_false(self):
        '''yatzy scores zero if numbers are different'''
        dice = yatzy.Yatzy(roll=[1,2,1,2,3], category="fours")
        self.assertEqual(0, dice.score())
    
    def test_pairs(self):
        '''score highest pair'''
        tests = [[3,3,3,4,4],
                 [1,1,6,2,6],
                 [3,3,3,4,1],
                 [3,3,3,3,1]]
        scores = [8, 12, 0, 0]
        results = [yatzy.Yatzy(test, "pairs").score() for test in tests]
        self.assertSequenceEqual(scores, results)
    
    def test_two_pairs(self):
        '''score sum of two pairs'''
        tests = [[1,1,2,3,3], [1,1,2,3,4], [1,1,2,2,2]]
        scores = [8, 0, 0]
        results = [yatzy.Yatzy(test, "two pairs").score() for test in tests]
        self.assertSequenceEqual(scores, results)
    
    def test_three_kind(self):
        '''score three of a kind'''
        tests = [[3,3,3,4,5], [3,3,4,5,6], [3,3,3,3,1]]
        scores = [9, 0, 0]
        results = [yatzy.Yatzy(test, "three of a kind").score() for test in tests]
        self.assertSequenceEqual(scores, results)
        
    def test_four_kind(self):
        '''score four of a kind'''
        tests = [[2, 2, 2, 2, 5], [2, 2, 2, 5, 5], [2, 2, 2, 2, 2]]
        scores = [8, 0, 0]
        results = [yatzy.Yatzy(test, "four of a kind"). score() for test in tests]
        self.assertSequenceEqual(scores , results)
        
    def test_small_straight(self):
        '''score a small straight'''
        self.assertEqual(15, yatzy.Yatzy([1, 2, 3, 4, 5], "small straight").score())
    
    def test_large_straight(self):
        '''score a large straight'''
        self.assertEqual(20, yatzy.Yatzy([2, 3, 4, 5, 6], "large straight").score())
    
    def test_full_house(self):
        '''score a full house'''
        tests = [[1,1,2,2,2], [2,2,3,3,4], [4,4,4,4,4]]
        scores = [8, 0, 0]
        results = [yatzy.Yatzy(test, "full house").score() for test in tests]
        self.assertSequenceEqual(scores, results)