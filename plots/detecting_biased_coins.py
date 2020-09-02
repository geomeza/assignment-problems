import sys
sys.path.append('src')
from coin_flipping import probability
import matplotlib.pyplot as plt
plt.style.use('bmh')

coin_1 = ['TTH', 'HHT', 'HTH', 'TTH', 'HTH', 'TTH', 'TTH', 'TTH', 'THT', 'TTH', 'HTH', 'HTH', 'TTT', 'HTH', 'HTH', 'TTH', 'HTH', 'TTT', 'TTT', 'TTT', 'HTT', 'THT', 'HHT', 'HTH', 'TTH']
coin_2 = ['HTH', 'HTH', 'HTT', 'THH', 'HHH', 'THH', 'HHH', 'HHH', 'HTT', 'TTH', 'TTH', 'HHT', 'TTH', 'HTH', 'HHT', 'THT', 'THH', 'THT', 'TTH', 'TTT', 'HHT', 'THH', 'THT', 'THT', 'TTT']
coin_3 = ['HHH', 'THT', 'HHT', 'HHT', 'HTH', 'HHT', 'HHT', 'HHH', 'TTT', 'THH', 'HHH', 'HHH', 'TTH', 'THH', 'THH', 'TTH', 'HTT', 'TTH', 'HTT', 'HHT', 'TTH', 'HTH', 'THT', 'THT', 'HTH']

coins = [coin_1, coin_2, coin_3]

def analyze_coin_flips(num_heads, coin_data):
    good_outcomes = 0
    for flip in coin_data:
        counter = flip.count('H')
        if counter == num_heads:
            good_outcomes += 1
    return good_outcomes/len(coin_data)

x_coords = [i for i in range(4)]
real_results = [probability(x, 3) for x in x_coords]
plt.plot(x_coords, real_results, linewidth=2.5)
for coin in coins:
    plt.plot(x_coords, [analyze_coin_flips(x, coin) for x in x_coords], linewidth=0.75)
plt.legend(['True','Coin 1','Coin 2','Coin 3'])
plt.xlabel('Number of Heads')
plt.ylabel('Real Probability')
plt.title('True Distribution vs Coins')
plt.savefig('bias_plot.png')
plt.show()

#Coin 2 looks normal, coin 1 seems to be biased towards tails and coin 3 biased towards heads