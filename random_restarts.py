from random import Random
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
bitset = 35
e = Evaluate(value, weights, maxWeight)
stop = StoppingCriteria(iterations=1000)

solutionsChecked = 0
restarts = 1000
solutionTuple = list()

for i in ini_sol.random_bitset(restarts, bitset):
    if e.evaluate(i)[0] > 0:
        x_curr = i
        x_best = x_curr[:]
        f_curr = e.evaluate(x_curr)
        f_best = f_curr[:]
        done = 0
        while done == 0:
            Neighborhood = nbor.one_m_flip_nbor(x_curr, 2)
            for s in Neighborhood:
                solutionsChecked += 1
                if e.evaluate(s)[0] > f_best[0]:
                    x_best = s[:]
                    f_best = e.evaluate(s)[:]
            if solutionsChecked > restarts:
                done = 1
            else:
                x_curr = x_best[:]
                f_curr = f_best[:]
        solutionTuple.append([x_curr, f_curr])

print("\nFinal number of solutions checked: ", solutionsChecked)
print(max(sol[1] for sol in solutionTuple))
# print("Best value found: ", f_best[0])
# print("Weight is: ", f_best[1])
# print("Total number of items selected: ", np.sum(x_best))
# print("Best solution: ", x_best)
