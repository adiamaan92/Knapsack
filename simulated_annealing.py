from random import Random  # need this for the random number generation -- do not change
import numpy as np
import math
from NeighborHood import NeighborHood
from InitSol import InitSol
from Evaluate import Evaluate
from StoppingCriteria import StoppingCriteria

seed = 5113
myPRNG = Random(seed)
n = 100
value = []
for i in range(0, n):
    value.append(myPRNG.uniform(10, 100))

weights = []
for i in range(0, n):
    weights.append(myPRNG.uniform(5, 20))

maxWeight = 5 * n
solutionsChecked = 0
nbor = NeighborHood(n, myPRNG)
ini_sol = InitSol(n, myPRNG)
e = Evaluate(value, weights,maxWeight)
stop = StoppingCriteria(iterations=1000)


# best-sol so far
# [3738.77800673, 499.4459, 47]
# Temperature = 100, alpha = 0.95
# Solution checked - 1000
# Neighbor - one_m_flip_nbor, m=4

solutionsChecked = 0
x_curr = ini_sol.zero_creator()[0]
x_best = x_curr[:]
f_curr = e.evaluate(x_curr)
f_best = f_curr[:]
done = 0
Temperature = 100
alpha = 0.95
iter_temp = 100


# various cooling schedule
# Linear scaling
def linear_scaling():
    global Temperature, alpha
    Temperature = alpha*Temperature


# Cauchy - schedule
def cauchy_schedule(k):
    global Temperature
    Temperature = (Temperature/(1+k))


# Boltzmann schedule
def boltzman_schedule(k):
    global Temperature
    Temperature = (Temperature/math.log(1+k))

while done == 0:
    k = 1
    for i in range(iter_temp):
        Neighborhood = nbor.one_m_flip_nbor(x_curr, 4)
        s = myPRNG.choice(Neighborhood)
        delta = (e.evaluate(s)[0] - e.evaluate(x_curr)[0])
        if delta > 0:
            x_best = s[:]
            f_best = e.evaluate(s)[:]
            x_curr = x_best[:]
            f_curr = f_best[:]
            solutionsChecked += 1
        else:
            if e.evaluate(s)[0] > 0:
                if myPRNG.random() < math.exp((delta/Temperature)):
                    x_best = s[:]
                    f_best = e.evaluate(s)[:]
                    x_curr = x_best[:]
                    f_curr = f_best[:]
                    solutionsChecked += 1
        if solutionsChecked == 1000:
            done = 1
    linear_scaling()
    k += 1
    print("\nTotal number of solutions checked: ", solutionsChecked)
    print("Best value found so far: ", f_best)

print("\nFinal number of solutions checked: ", solutionsChecked)
print("Best value found: ", f_best[0])
print("Weight is: ", f_best[1])
print("Total number of items selected: ", np.sum(x_best))
print("Best solution: ", x_best)
