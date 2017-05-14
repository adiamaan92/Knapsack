from random import Random
import numpy as np
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

max_weight = 5 * n
solutionsChecked = 0
nbor = NeighborHood(n, myPRNG)
ini_sol = InitSol(n, myPRNG)
e = Evaluate(value, weights, max_weight)
stop = StoppingCriteria(iterations=10000)

solutionsChecked = 0
x_curr = ini_sol.zero_creator()[0]
x_best = x_curr[:]
f_curr = e.evaluate(x_curr)
f_best = f_curr[:]
done = 0
k = 1

while done == 0:
    k = 1
    while k < 4:
        if k == 1:
            Neighborhood = nbor.one_flip_nbor(x_curr)
        elif k == 2:
            Neighborhood = nbor.one_m_flip_nbor(x_curr, 4)
        elif k == 3:
            Neighborhood = nbor.sad_nbor(x_curr, 6)
        else:
            NeighborHood = nbor.m_flip_nbor(x_curr, 2)
        s = myPRNG.choice(Neighborhood)
        solutionsChecked += 1
        if e.evaluate(s)[0] > f_best[0]:
            x_best = s[:]
            f_best = e.evaluate(s)[:]
            k = 1
        if stop.stop_stagnation(f_best):
            done = 1
            k = 5
        else:
            x_curr = x_best[:]
            f_curr = f_best[:]
            k += 1
            print("\nTotal number of solutions checked: ", solutionsChecked)
            print("Best value found so far: ", f_best)

print("\nFinal number of solutions checked: ", solutionsChecked)
print("Best value found: ", f_best[0])
print("Weight is: ", f_best[1])
print("Total number of items selected: ", np.sum(x_best))
print("Best solution: ", x_best)
