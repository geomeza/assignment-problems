findSmallestPositive :: (Num a, Ord a) => [a] -> a

findSmallestPositive [] = error "min of empty list"  
findSmallestPositive [x] = x  
findSmallestPositive (x:xs)   
    |x>0 &&  x < min = x  
    |otherwise = min
    where min =findSmallestPositive xs

main = print (findSmallestPositive [8, 3, -1, 2, -5, 7])