import random

a = random.sample(range(1,30), 12)
print(a)
b = random.sample(range(1,30), 16)
print(b)

results_overlap = [i for i in set(a) if i in b]
result = [i for i in results_overlap if results_overlap.count(i) == 1]

print (results_overlap)