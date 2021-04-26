from random import sample

class Enos2:
    
    def __init__(self, digits=4):
        self.digits = digits
        self.renew()
    
    # guess next 4 digits in list
    # last is in tuple with 2 int, first for number of A, second for number of B
    def guess(self, last=None):
        if last:
            self.count += 1
            self.ab.append(last)
        g = self._ai()
        self.g.append(g)
        
        return g

    def renew(self):
        self.count = 0
        self.g = []
        self.ab = []

    # some great logic
    def _ai(self):
        digits = set(range(10))
        for c in range(self.count):
            if sum(self.ab[c]) == self.digits:
                digits = set(self.g[c])
                break
            if self.ab[c] == (0,0):
                for v in self.g[c]:
                    digits.discard(v)
        
        return sample(digits, k=self.digits)
