from random import Random
import numpy as np
from InitSol import InitSol
from NeighborHood import NeighborHood


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
ini_sol = InitSol(n, myPRNG)
nbor = NeighborHood(n, myPRNG)


def evaluate(x):
    a = np.array(x)
    b = np.array(value)
    c = np.array(weights)
    totalValue = np.dot(a, b)
    totalWeight = np.dot(a, c)
    if totalWeight > maxWeight:
        return [-1, -1]
    return [totalValue, totalWeight]  # returns a list of both total value and total weight

solutionsChecked = 0
x_curr = ini_sol.zero_creator()[0]
x_best = x_curr[:]
f_curr = evaluate(x_curr)
f_best = f_curr[:]

done = 0
while done == 0:
    Neighborhood = nbor.one_m_flip_nbor(x_curr, 4)
    for s in Neighborhood:
        solutionsChecked += solutionsChecked
        if evaluate(s)[0] > f_best[0]:
            x_best = s[:]
            f_best = evaluate(s)[:]
            break
    if solutionsChecked >= 10000:
        done = 1
    else:
        x_curr = x_best[:]
        f_curr = f_best[:]
        print("\nTotal number of solutions checked: ", solutionsChecked)
        print("Best value found so far: ", f_best)

print("\nFinal number of solutions checked: ", solutionsChecked)
print("Best value found: ", f_best[0])
print("Weight is: ", f_best[1])
print("Total number of items selected: ", np.sum(x_best))
print("Best solution: ", x_best)
