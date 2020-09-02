import sys
sys.path.append('src')
from coin_flipping import monte_carlo_probability,probability


print('--- Normal Probability ---')
print(probability(5,8))
print('--- Monte Carlo Probabilities ---')
for i in range(3):
    print(monte_carlo_probability(5,8))
