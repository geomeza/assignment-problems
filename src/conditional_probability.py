from coin_flipping import probability
import math
flips = {
    'George': 'THTH HTHT THTH HHTH THTH TTHT THTH TTTH THTH TTHT THHT HTTH THTH THHT THHT THTH THTH THHT THTH THTH',
    'David': 'TTHH HHTT HHTT TTHH HTHT THTH THTH THTH HTHT HTHT THTH HTHT THHH THTH HHTT HHTT TTTH HHTH HTHH TTTH',
    'Elijah': 'THTT HTHT HTHH HHHT TTHH THHH TTTT HHTT TTTH TTHH HTHT HTHT TTTT HTTT TTTH HTTT TTHH THTH THHH HTHH',
    'Colby': 'HTTH HTHH THTT HHTH TTHT HTTT THHH TTHH HHTT THTH HHTT THTH THHH TTHH THTT HHTH HTTH HTHH TTHT HTTT',
    'Justin': 'THTT HTHT TTTH THHT HTHH TTTH THTH HHTH TTTT HTTH HHTT THHH HHHH THTH HTTH TTHH HTHT HHHT THHT TTTH'
}
names = ['George', 'David', 'Elijah', 'Colby', 'Justin']
total_flip_sequences = []
for elem in flips.values():
    total_flip_sequences.append(elem)

split_flip_sequences = []
for person_flip_sequences in total_flip_sequences:
    split_sequences = person_flip_sequences.split(' ')
    split_flip_sequences.append(split_sequences)

def split_into_pairs(sequence):
    return [[sequence[i], sequence[i+1]] for i in range(len(sequence) - 1)]


def count_outcomes(data, prev, next):
    prev_count = 0
    both_count = 0
    for sequence in data:
        pairs = split_into_pairs(sequence)
        for pair in pairs:
            if pair[0] == prev:
                prev_count += 1
                if pair[1] == next:
                    both_count += 1
    return both_count/prev_count

possibilites = [['H', 'H'], ['T', 'H'], ['H', 'T'], ['T', 'T']]

for i in range(len(names)):
    print('--------------------------------')
    print('\n', names[i], 'Probability:')
    for p in possibilites:
        print('\n---------------------')
        print('\nPosibility of (next flip',p[0],'| previous', p[1],')')
        print(count_outcomes(split_flip_sequences[i], p[1], p[0]))
        print('\n---------------------')
    print('\n--------------------------------')

print('Test String')
dataset = ['HHTTHT']
for p in possibilites:
    print('\n---------------------')
    print('\nPosibility of (next flip',p[0],'| previous', p[1],')')
    print(count_outcomes(dataset, p[1], p[0]))
    print('\n---------------------')
