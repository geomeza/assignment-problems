from coin_flipping import probability,flip_coin
import math


def coin_flip_tests(num_flips, num_of_tests):
    return [flip_coin(num_flips) for _ in range(num_of_tests)]

def calculate_distribution(num_heads, tests):
    good_outcomes = 0
    for test in tests:
        counter = test.count('H')
        if counter == num_heads:
            good_outcomes += 1
    return good_outcomes/len(tests)

def total_distribution(num_flips, num_of_tests):
    data_set = coin_flip_tests(num_flips, num_of_tests)
    distribution = []
    for i in range(num_flips + 1):
        distribution.append(calculate_distribution(i, data_set))
    return distribution

def kl_divergence(p,q):
    return sum([p[i]*(math.log(p[i]/q[i])) for i in range(len(p))])

def non_zeros(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = 0.0001
    return nums

p = [0.2, 0.7, 0.1]
q = [0.1, 0.8, 0.1]
assert round(kl_divergence(p,q),11) == 0.04515746127, ('KL divergence does not work should be',0.04515746127,'got',round(kl_divergence(p,q),11))

real_results = non_zeros([probability(x, 5) for x in range(6)])
monte_carlo_100 = non_zeros(total_distribution(5, 100))
monte_carlo_1000 = non_zeros(total_distribution(5, 1000))
monte_carlo_10000 = non_zeros(total_distribution(5, 10000))

print("Divergence with 100 trials: ")
print(kl_divergence(monte_carlo_100, real_results))
print("\nDivergence with 1000 trials: ")
print(kl_divergence(monte_carlo_1000, real_results))
print("\nDivergence with 10000 trials: ")
print(kl_divergence(monte_carlo_10000, real_results))

