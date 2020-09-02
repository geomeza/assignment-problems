from coin_flipping import probability

def expected_value(x,probabilities): ## PROBABILITIES IS THE DISTRIBUTION OF POSSIBILITES
    val = 0
    for i in range(len(x)): ## SUMMING EVERY X TIMES THE PROBABILITY OF THAT X HAPPENING
        val += x[i]*probabilities[i]
    return val

def variance(x, distribution):
    expected_val = expected_value(x, distribution) ## FINDING EXPECTED VALUE
    variance = sum([((x[i]-expected_val)**2)*distribution[i] for i in range(len(x))]) ## SUMMING THE NUM OF HEADS MINUS THE EXPECTED VALUE AND SQUARING IT THEN MLTIPLYING BY THE PROBABILTY OF GETTING THAT AMOUNT OF HEADS IN A SEQUENCE FOR EVERY AMOUNT OF HEADS IN THE RANGE OF 4
    return variance

def st_dev(x, distribution):
    return math.sqrt(variance(x, distribution))
x = [0,1,2,3,4]

distribution = [probability(i,4) for i in range(len(x))] ## USING PRE MADE PROBABILITY FUNCTION
print('\nA1----------')
print('\nProbability of getting x heads in 4 flips')
for i in range(len(distribution)):
    print(i,':',distribution[i])
print('\nA2----------')
print('\nProbably 2 because it is the biggest chance of actually happening')
print('\nA3----------')
print('\nExpected value of X is', expected_value(x, distribution))
print('\nA4----------')
print('\nVariance is ', variance(x, distribution))
print('\nA5----------')
print('\nStandard Deviation is ', variance(x, distribution))
print('\n')
print('\nB1----------')
distribution = ['(1-λ)^4', '4λ(1-λ)^3', '6λ^2(1-λ)^2', '4λ^3(1-λ)', 'λ^4']
for i in range(len(distribution)):
    print(i,':',distribution[i])
print('\nB2----------')
print('\nIt would be 4 times lambda because its the amount of flips times the probability')
print('\nB3----------')
print('\n Expected:')
print('\n 0 * (1 - λ)^4 + 1 * (4 λ (1 - λ)^3) + 2 * (6 λ^2 (1 - λ)^2) + 3 * (4 λ^3 (1 - λ)) + 4 * λ^4')
print('\n (4 * (1 - λ)^3) + 2 * (6 λ^2 (1 - λ)^2) + 3 * (4 λ^3 (1 - λ)) + 4x^4')
print('\n (4 * (1 - λ)^3) + 2 * (6 λ^2 (1 - λ)^2) + 12λ^3 - 12λ^4 + 4 λ^4')
print('\n (4x * (1 - 3 λ + 3 λ^2 - λ^3) + 2 * (6λ^2 (1 - 2 λ + λ^2)) + 12λ^3 - 12λ^4 + 4 λ^4')
print('\n 4λ - 12λ^2 + 12λ^3 - 4λ^4 + 12λ^2 - 24λ^3 + 12λ^4 + 12λ^3 - 12λ^4 + 4λ^4')
print('\n 4λ')
print('\nB4----------')
print('\nVariance:')
print('\n((0 - 4λ)^2 * (1-λ)^4) + ((1 - 4λ)^2 * 4λ(1-λ)^3) + ((2 - 4λ)^2 * 6λ^2(1-λ)^2) + ((3 - 4λ)^2 * 4λ^3(1-λ)) + ((4 - 4λ)^2 * λ^4)')
print('\nB5----------')

print('\n((0 - 4λ)^2 * (1-λ)^4) + ((1 - 4λ)^2 * 4λ(1-λ)^3) + ((2 - 4λ)^2 * 6λ^2(1-λ)^2) + ((3 - 4λ)^2 * 4λ^3(1-λ)) + ((4 - 4λ)^2 * λ^4)')
print('\nSquare root of that ^^^^^^^^')




