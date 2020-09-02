import random

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num*factorial(num - 1)

def combination(n, k):
    return factorial(n)/(factorial(k) * factorial(n - k))

def flip_coin(num_flips):
    flip_sequence = ''
    for i in range(num_flips):
        flip_sequence += random.choice(['T','H'])
    return flip_sequence

def probability(num_heads, num_flips):
    outcomes = 2**num_flips
    probability = combination(num_flips, num_heads)
    return probability/outcomes

def monte_carlo_probability(num_heads, num_flips, range_of_tests = 1000):
    good_outcomes = 0
    for i in range(range_of_tests):
        heads = 0
        flipped = flip_coin(num_flips)
        if flipped.count('H') == num_heads:
            good_outcomes += 1
    return good_outcomes/range_of_tests