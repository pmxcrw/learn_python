class Yatzy(object):
        
    def __init__(self, roll, category):
        self.roll = roll
        self.category = category
    
    def score(self):
        
        singles = {'ones': 1, 'twos': 2, 'threes': 3, 'fours': 4, 'fives': 5, 'sixes': 6}

        if self.category == "chance":
            return sum(self.roll)
        
        if self.category == "small straight" and self.roll == [1, 2, 3, 4, 5]:
            return 15
        
        if self.category == "large straight" and self.roll == [2, 3, 4, 5, 6]:
            return 20
        
        elif self.category == "yatzy":
            same_nums = True
            for i in range(len(self.roll) - 1):
                if self.roll[i] != self.roll[i+1]:
                    same_nums = False
                    break
            if same_nums:
                return 50
            else:
                return 0
        
        elif self.category in singles:
            score = 0
            for die in self.roll:
                if die == singles[self.category]:
                    score += die
            return score
        
        elif self.category in {"pairs", "three of a kind", "four of a kind"}:
            for i in range(max(self.roll), 0, -1):
                count = sum([die == i for die in self.roll])
                if count == 2 and self.category == "pairs":
                    return 2 * i
                elif count == 3 and self.category == "three of a kind":
                    return 3 * i
                elif count == 4 and self.category == "four of a kind":
                    return 4 * i
            else:
                return 0
        
        elif self.category == "two pairs":
            for i in range(max(self.roll), 0, -1):
                higher_count = sum([die == i for die in self.roll])
                if higher_count == 2:
                    for j in range(i-1, 0, -1):
                        lower_count = sum([die == j for die in self.roll])
                        if lower_count == 2:
                            return 2 * (i + j)
            else:
                return 0

        elif self.category == "full house":
            
            sorted_roll = self.roll
            sorted_roll.sort()
            ends = False
            centre = False
            
            if sorted_roll[-1] == sorted_roll[-2] and sorted_roll[0] == sorted_roll[1]:
                ends = True   
                if sorted_roll[-2] == sorted_roll[-3] and sorted_roll[1] != sorted_roll[2]:
                    return sum(self.roll)
                elif sorted_roll[-2] != sorted_roll[-3] and sorted_roll[1] == sorted_roll[2]:
                    return sum(self.roll)

            return 0