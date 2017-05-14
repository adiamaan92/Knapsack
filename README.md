# Knapsack
Solving a random Instance of the Knapsack problem (n = 100) using Neighborhood based Meta-heuristic Models.

A random instance of a knapsack problem is chosen and we try to maximize the total value without exceeding the weight limitation which is n*5.

The code is modularized with each Neighborhood algorithm residing in a seperate file and the operations such as evaluate function, stopping criteria and Initial solution kept in seperate files to avoid redundancy and provide ways to add more ways.

This particular instance of the knapsack problem was solved using AMPL and the global maxima was found to be 3738.67. Our main objective is to tune the model so that they achieve this global maxima.

InitSol.py – This is a class which has the two initial solution functions,
• Zero_creator: Generates all zeros as the initial solution
• Random_bitset: Randomly set m bits as 1 in the total of 100 bits

Evaluate.py – This is a class which has the following evaluate functions,
• evaluate: This function checks for the feasibility and return the total value and total weight if feasible and [-1, -1] if infeasible. This handles infeasibility and makes sure that solution is never chosen.
• Tabu_evaluate: This function is used for evaluating the neighbour during the tabu search.

Neighbourhood.py – This is a class which exposes the following neighbourhoods
• One Flip Neighbourhood: In this method we flip each of the bits in our current solution and append that to our neighbourhood list for that specific current solution.
• One, N Flip Neighbourhood: In this method, we use one flip first and we randomly flip m more bits. The randomness shakes up getting stuck in the local optima and gets to the global optima. The neighbourhood size remains n.
• Swap, Add or Delete Neighbourhood: Based on a random choice one of the three operations 1) swap, 2) add an element 3) delete an element is performed. For swap two random positions are generated and for 2 and 3 a random position is selected and set to 1 and 0. z is the number of times this random operation is performed. Abbreviation: sad - swap, add or delete.
• N Flip Neighbourhood: In this method we flip two bits in our current solution. Compared to one flip neighbourhood this has a much larger size of 100Cn. It increases exponentially as n increases.

StoppingCriteria.py – This is a class that exposes stop_stagnation function that uses the algorithm getting stagnated for n iterations and stops the algorithm. This can be called in any algorithm and can be used as a stopping criteria.
The other file names are self-explanatory.

Summary:
Best Improvement – 3690.35
First Improvement – 3672
Random restarts – 3724.01
Random walk – 3657
Simulated Annealing – 3738.79
Tabu Search – 3704.28
VNS – 3705.

We achieved Global maxima using Simulated Annealing.!
