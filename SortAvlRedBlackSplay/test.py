import random
from time import time

from structures.AVLTree import AVLTree

arr = []

for i in range(500000):
    arr.append(random.randint(1, 10000000))

l = []
tr = AVLTree()

_t1 = time()
for num in arr:
    l.append(num)
_t2 = time()

_t3 = time()
for num in arr:
    tr.insert(num)
_t4 = time()

print(f"time_l = {_t2 - _t1}")
print(f"time_tr = {_t4 - _t3}")
