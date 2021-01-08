import sys
sys.path.append('src')
from random_draw import random_draw

distributions = [[0.5, 0.5],[0.25, 0.25, 0.5],[0.05, 0.2, 0.15, 0.3, 0.1, 0.2]]
for dist in distributions:
    draws = []
    new_distribution = []
    for i in range(10000):
        draws.append(random_draw(dist))
    for i in range(len(dist)):
        new_distribution.append(draws.count(i)/10000)
    print('Distribution Test:', dist)
    print('Average Distribution:',new_distribution )