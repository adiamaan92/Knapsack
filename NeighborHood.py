import itertools


class NeighborHood(object):

    # Constructor for NeighborHood class
    def __init__(self, num_of_neighbor, random_gen):
        self.n = num_of_neighbor
        self.myPRNG = random_gen

    # One-flip Neighborhood
    def one_flip_nbor(self, x):
        nbrhood = []
        for i in range(0, self.n):
            nbrhood.append(x[:])
            if nbrhood[i][i] == 1:
                nbrhood[i][i] = 0
            else:
                nbrhood[i][i] = 1
        return nbrhood

    # m-flip Neighborhood
    def m_flip_nbor(self, x, m):
        nbrhood = []
        for i, j in itertools.combinations(range(0, self.n), m):
            xtemp = x[:]
            if xtemp[i] == 1:
                xtemp[i] = 0
            else:
                xtemp[i] = 1
            if xtemp[j] == 1:
                xtemp[j] = 0
            else:
                xtemp[j] = 1
            nbrhood.append(xtemp)
        return nbrhood


    # One-flip, m flip Neighborhood where after the 1 flip
    # m random bits are again flipped. 1,n flip Neighborhood
    # The randomness shakes up getting stuck in the local optima and gets the global optima
    def one_m_flip_nbor(self, x, m):
        nbrhood = []
        for i in range(0, self.n):
            nbrhood.append(x[:])
            if nbrhood[i][i] == 1:
                nbrhood[i][i] = 0
            else:
                nbrhood[i][i] = 1
            for v in range(self.myPRNG.randint(0,m)):
                randi = self.myPRNG.randint(0,99)
                if nbrhood[i][randi] == 1:
                    nbrhood[i][randi] = 0
                else:
                    nbrhood[i][randi] = 1
        return nbrhood

    # Based on a random choice one of the three operations 1) swap, 2) add an element 3) delete an element
    # is performed. For swap two random positions are generated and for 2 and 3 a random position is selected and
    # set to 1 and 0. z is the number of times this random operation is performed
    # sad - swap, add or delete

    def sad_nbor(self, x, z):
        nbhood = []
        for i in range(0, self.n):
            for c in range(self.myPRNG.randint(1, z)):
                option = self.myPRNG.randint(0, 2)
                m = self.myPRNG.randint(0, 99)
                if option == 0:
                    o = self.myPRNG.randint(0, 99)
                    x[m], x[o] = x[o], x[m]
                elif option == 1:
                    x[m] = 1
                elif option == 2:
                    x[m] = 0
                nbhood.append(x)
        return nbhood