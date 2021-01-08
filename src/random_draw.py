import random

def into_cumulative(distribution):
    for i in range(len(distribution)):
        if i > 0:
            distribution[i] += distribution[i-1]
    return distribution

def random_draw(distribution):
    new_dist = [num for num in distribution]
    cumulative_dist = into_cumulative(new_dist)
    choice = random.random()
    for x in cumulative_dist:
        if choice > x:
            pass
        else:
            return cumulative_dist.index(x)
