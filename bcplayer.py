from random import sample

class Bcplayer:

    # digits set the digit number of a game
    def __init__(self, digits=4):
        self.digits = digits
        self.renew()
    
    # guess next 4 digits in list
    # last is in tuple with 2 int, first for number of A, second for number of B
    def guess(self, last=None):
        return sample(range(10), k=self.digits)
    
    # will be called for a new game
    def renew(self):
        pass
