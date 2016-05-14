import numpy as np

class Zekendorf(object):
    
    def __init__(self):
        self.fibs = [1, 2]
        
    def update_fibs(self, n):
        while n > self.fibs[-1] + self.fibs[-2]:
            new_fib = self.fibs[-1] + self.fibs[-2]
            self.fibs.append(new_fib)
    
    def single_zek(self, n):
        self.update_fibs(n)
        return self._zek(n)
    
    def _zek(self, n, fibs = []):
        result = ""
        if fibs == []:
            fibs = self.fibs
        for fib in fibs[::-1]:
            if fib <= n:
                result += "1"
                n -= fib
            elif len(result) > 0:
                result += "0"
        return int(result)
    
    def zek_table(self, n):
        self.update_fibs(n)
        fibs = np.array(self.fibs)
        output = ""
        for i in range(1, n+1):
            truncate = fibs.searchsorted(i)
            zek = self._zek(i, fibs[:truncate + 1])
            print(zek)
    
z = Zekendorf()
z.zek_table(1000)
            
            
        