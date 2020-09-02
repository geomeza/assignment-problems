import sys
sys.path.append('src')
from coin_flipping import monte_carlo_probability,probability
import matplotlib.pyplot as plt
plt.style.use('bmh')

num_heads = [0,1,2,3,4,5,6,7,8,9,10]
true_result = [probability(x,10) for x in num_heads]

mc_1 = [monte_carlo_probability(x,10) for x in num_heads]
mc_2 = [monte_carlo_probability(x,10) for x in num_heads]
mc_3 = [monte_carlo_probability(x,10) for x in num_heads]
mc_4 = [monte_carlo_probability(x,10) for x in num_heads]
mc_5 = [monte_carlo_probability(x,10) for x in num_heads]

plt.plot(num_heads, true_result, linewidth=2.5)
plt.plot(num_heads, mc_1, linewidth=0.75)
plt.plot(num_heads, mc_2, linewidth=0.75)
plt.plot(num_heads, mc_3, linewidth=0.75)
plt.plot(num_heads, mc_4, linewidth=0.75)
plt.plot(num_heads, mc_5, linewidth=0.75)

plt.legend(['True','MC 1','MC 2','MC 3', 'MC 4', 'MC 5'])
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('True Distribution vs Monte Carlo Simulations for 10 Coin Flips')
plt.savefig('coin_plot.png')
plt.show()