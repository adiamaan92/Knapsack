from random import Random
import numpy as np
import operator
from InitSol import InitSol
from NeighborHood import NeighborHood
from Evaluate import Evaluate

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

solutionsChecked = 0
restarts = 10000
solutionTuple = list()
probCheck = 0.75
x_curr = ini_sol.zero_creator()[0]
x_best = x_curr[:]
f_curr = e.evaluate(x_curr)
f_best = f_curr[:]

best_sol = list()
done = 0
while done == 0:
    Neighborhood = nbor.one_flip_nbor(x_curr)
    probRand = myPRNG.random()
    solution_picked = 0
    if probRand > probCheck:
        while solution_picked == 0:
            solutionsChecked += 1
            x_curr = myPRNG.choice(Neighborhood)
            if e.evaluate(x_curr)[0] >= 0:
                x_best = x_curr[:]
                f_curr = e.evaluate(x_curr)
                f_best = f_curr
                solution_picked = 1
                best_sol.append(f_best)
    else:
        for s in Neighborhood:
            solutionsChecked += 1
            if e.evaluate(s)[0] > f_best[0]:
                x_best = s[:]
                f_best = e.evaluate(s)[:]
                best_sol.append(f_best)
        if solutionsChecked >= 30000:
            done = 1
        else:
            x_curr = x_best[:]
            f_curr = f_best[:]
    print("\nTotal number of solutions checked: ", solutionsChecked)
    print("Best value found so far: ", f_best)

print(max(enumerate(best_sol), key=operator.itemgetter(1)))

print("\nFinal number of solutions checked: ", solutionsChecked)
print("Best value found: ", f_best[0])
print("Weight is: ", f_best[1])
print("Total number of items selected: ", np.sum(x_best))
print("Best solution: ", max(best_sol))
