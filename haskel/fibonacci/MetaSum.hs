nthFib :: Integer->Integer
nthFib 1 = 1
nthFib 0 = 0  
nthFib n = nthFib (n-1) + nthFib (n-2)

partialSumEntries n = map(nthFib) [0..n]

partialSum n = sum(partialSumEntries n) 

metaSum n = sum(map(partialSum) (partialSumEntries n))

main = print(metaSum 6)