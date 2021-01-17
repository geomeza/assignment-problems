nthFibonacci :: Integer->Integer
nthFibonacci 1 = 1
nthFibonacci 0 = 0  
nthFibonacci n = nthFibonacci (n-1) + nthFibonacci (n-2)

main = print (nthFibonacci 20)