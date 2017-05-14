import random

def initial_solution(n):
    for i in range(n):
        temp = random.sample(range(1, 11), 2)
        yield [1 if x in temp else 0 for x in range(1, 11)]

for i in initial_solution(5):
    print(i)

print(random.rand())