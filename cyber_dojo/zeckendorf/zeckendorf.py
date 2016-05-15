import numpy as np

class Zeckendorf(object):
    
    def __init__(self):
        self.fibs = [1, 2]
        
    def update_fibs(self, n):
        while n >= sum(self.fibs[-2:]):
            new_fib = sum(self.fibs[-2:])
            self.fibs.append(new_fib)
    
    def single_zek(self, n):
        self.update_fibs(n)
        result = ""
        for fib in self.fibs[::-1]:
            if fib <= n:
                result += "1"
                n -= fib
            elif len(result) > 0:
                result += "0"
        return int(result)
    
    def zek_table(self, n):
        output = "1:\t1"
        for i in range(2, n+1):
            zek = self.single_zek(i)
            output += "\n{}:\t{}".format(i, zek)
        return output
