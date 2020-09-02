from coin_flipping import probability
import math
flips = {
    'George': 'THTH HTHT THTH HHTH THTH TTHT THTH TTTH THTH TTHT THHT HTTH THTH THHT THHT THTH THTH THHT THTH THTH ',
    'David': 'TTHH HHTT HHTT TTHH HTHT THTH THTH THTH HTHT HTHT THTH HTHT THHH THTH HHTT HHTT TTTH HHTH HTHH TTTH ',
    'Elijah': 'THTT HTHT HTHH HHHT TTHH THHH TTTT HHTT TTTH TTHH HTHT HTHT TTTT HTTT TTTH HTTT TTHH THTH THHH HTHH ',
    'Colby': 'HTTH HTHH THTT HHTH TTHT HTTT THHH TTHH HHTT THTH HHTT THTH THHH TTHH THTT HHTH HTTH HTHH TTHT HTTT ',
    'Justin': 'THTT HTHT TTTH THHT HTHH TTTH THTH HHTH TTTT HTTH HHTT THHH HHHH THTH HTTH TTHH HTHT HHHT THHT TTTH '
}

flip_sequences = []
for elem in flips.values():
    flip_sequences.append(elem)

def sort_flip_sequences(unsorted_flip_sequences):
    all_sorted = []
    for i in range(len(unsorted_flip_sequences)):
        sorted_sequences = []
        buffer = ''
        counter = 0
        for flip in unsorted_flip_sequences[i]:
            counter += 1
            if flip != ' ':
                buffer+= flip
            if counter%5 == 0:
                sorted_sequences.append(buffer)
                buffer = ''
        all_sorted.append(sorted_sequences)
    return all_sorted

names = ['George', 'David', 'Elijah', 'Colby', 'Justin']
sorted_flip_sequences = sort_flip_sequences(flip_sequences)

def kl_divergence(p,q):
    divergence = 0
    for i in range(len(p)):
        if p[i] != 0:
            divergence +=p[i]*(math.log(p[i]/q[i]))
    return divergence

def calculate_distribution(num_heads, tests):
    good_outcomes = 0
    for test in tests:
        counter = test.count('H')
        if counter == num_heads:
            good_outcomes += 1
    return good_outcomes/len(tests)

def total_distribution(num_flips, data):
    data_set = data
    distribution = []
    for i in range(num_flips + 1):
        distribution.append(calculate_distribution(i, data_set))
    return distribution

real_results = [probability(x,4) for x in range(5)]
for i in range(len(sorted_flip_sequences)):
    distribution = total_distribution(4, sorted_flip_sequences[i])
    round_distribution = [round(elem, 9) for elem in distribution]
    print('-------------------------')
    print('\nKL DIVERGENCE FOR', names[i],':')
    print('\n',kl_divergence(round_distribution, real_results))
    print('\n-------------------------')

print('Justin got the lowest divergence so his is most accurate')
