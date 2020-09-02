import matplotlib.pyplot as plt
plt.style.use('bmh')

def calculate_likelihood(flip_sequence, heads_probability):
    if isinstance(heads_probability, float): ## CHECKS IF PROBABILITY IS DECIMALS OR NOT
        likelihood = 1 ## STARTS AS ONE BECAUSE PROBABILITIES WILL GET MULTIPLIED TO IT
        tails_probability = 1 - heads_probability ## PROBABILITY OF LANDING TAILS
        for flip in flip_sequence: ## CHECKS EVERY FLIP IN SEQUENCE
            if flip == 'T': ## CHECKS IF FLIP IS HEADS OR NOT
                likelihood *= tails_probability ## MULTIPLIES LIKELIHOOD BY PROBABILITES
            else:
                likelihood *= heads_probability
        return likelihood ## RETURNS TOTAL LIKELIHOOD
    else:
        tails_count = flip_sequence.count('T') ## COUNTS AMOUNT OF TAILS AND HEADS IN SEQUENCE
        heads_count = flip_sequence.count('H')
        result = '(p) ^ ' + str(heads_count) + ' * (1-p) ^ '+ str(tails_count) ## STRING OF TOTAL LIKELIHOOD
        return result ## RETURNS STRING

likelihood = [0.5, 0.55,'p'] ## SETUP FOR FOR LOOP
flip_sequence = 'HHTTH'

print('\nSEQUENCE IS:', flip_sequence) ## PRINTING SEQUENCE
for l in likelihood:
    print('\nLikelihood for coin with', l, 'probability of heads') ## PRINT StATemEnts
    result = calculate_likelihood(flip_sequence,l)
    if isinstance(result, float):
        print('\n',round(result, 5))
    else:
        print(result)

x = 0.01
x_coords = [0.01]
while x < 1:
    x += 0.01
    x_coords.append(round(x, 2)) ## MAKING ALL X COORDINATES
likelihood_with_x = [round(calculate_likelihood(flip_sequence, x),5) for x in x_coords] ## CALCULATING ALL LIKELIHOODS
plt.plot(x_coords, likelihood_with_x, linewidth = 2.5) ## A TON OF GRAPHING STUFF
plt.legend(['Varied likelihood'])
plt.xlabel('Probability of getting heads')
plt.ylabel('likelihood')
plt.title('Likelihood graph')
plt.savefig('likelihood.png')
plt.show()
