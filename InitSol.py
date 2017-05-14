class InitSol(object):

    def __init__(self, n, myPRNG):
        self.n = n
        self.myPRNG = myPRNG

    # A simple initial solution that st
    def zero_creator(self):
        x = list()
        x.append([0 for i in range(self.n)])
        return x

    # A initial solution generator that generates n random initial solution
    # with bits randomly placed at m positions
    # m = 35 works best for random restart so far
    def random_bitset(self, n, m):
        for i in range(self.n):
            temp = self.myPRNG.sample(range(1, 101), self.myPRNG.randint(1, m))
            yield [1 if x in temp else 0 for x in range(1, 101)]

