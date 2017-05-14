from random import Random  # need this for the random number generation -- do not change
import numpy as np
from collections import deque
import operator
from NeighborHood import NeighborHood
from InitSol import InitSol
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

# best-sol so far (7569, 3704.2885640312543)
# tabu tenure - 5, short term solution -10
# total solutions checked - 1000
# Neighbor - one_m_flip_nbor, m =2

solutionsChecked = 0
x_curr = ini_sol.zero_creator()[0]
x_best = x_curr[:]
f_curr = e.tabu_eval(x_curr)
f_best = f_curr
done = 0

long_term_best = list()
short_term_sol = 10
visited_solution = deque(maxlen=short_term_sol)
tabu_tenure = 5
tabu_bitset = [0 for i in range(n)]
asp_flag = True
visited_solution.append(x_curr)


def frame_mod(neigh, x_curr):
    global tabu_bitset, visited_solution
    neigh = [x for x in neigh if x not in visited_solution and e.tabu_eval(x) >= 0]
    truncated_neigh = list()
    for i in neigh:
        add_flag = False
        for j in range(len(i)):
            if tabu_bitset[j] != 0 and i[j] == x_curr[j]:
                add_flag = True
            elif tabu_bitset[j] == 0:
                add_flag = True
            else:
                add_flag = False
                break
        if add_flag:
            truncated_neigh.append(i)
    return truncated_neigh


def sub_routine(nbhood, f_curr):
    global x_curr, x_best, f_best, tabu_bitset, visited_solution, n, asp_flag
    sol_value = [e.tabu_eval(x) for x in nbhood]
    if len(sol_value) == 0:
        asp_flag = False
        return
    max_index, max_value = max(enumerate(sol_value), key=operator.itemgetter(1))
    while e.tabu_eval(nbhood[max_index]) < -1:
        sol_value.remove(max_value)
        max_index, max_value = max(enumerate(sol_value), key=operator.itemgetter(1))
    if max_index == -1 or None:
        asp_Flag = False
        return
    x_best = nbhood[max_index]
    f_best = max_value
    visited_solution.append(x_best)
    for i in range(n):
        if x_curr[i] != x_best[i]:
            tabu_bitset[i] = tabu_tenure

while done == 0 and solutionsChecked < 10000:
    tabu_bitset = [0 if x == 0 else x-1 for x in tabu_bitset]
    asp_flag = True
    solutionsChecked += 1
    Neighborhood = nbor.m_flip_nbor(x_curr, 2)
    mod_neighborhood = frame_mod(Neighborhood, x_curr)
    asp_neighborhood = [m for m in Neighborhood if m not in mod_neighborhood and m not in visited_solution and e.tabu_eval(m) >= 0 ]
    sub_routine(mod_neighborhood, f_curr)
    if not asp_flag:
        sub_routine(asp_neighborhood, f_curr)
        tabu_bitset = [0 for i in range(n)]
        for z in range(n):
            if x_best[z] == 1:
                tabu_bitset[z] = tabu_tenure
    if f_best == f_curr:
        done = 1
    else:
        x_curr = x_best
        f_curr = f_best
        long_term_best.append([x_best, f_best])
    print("Total Solution iterated : ", solutionsChecked)
    print("Best Value found so far : ", f_best)


print(max(enumerate([row[1] for row in long_term_best]), key=operator.itemgetter(1)))
