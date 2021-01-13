makeList n = length [(x,y) | x <- [-n..n], y <-[-n..n], x-y <= (x*y)/2, (x*y)/2 <= x+y, x/= 2, y/= 2, x/= 1,x/= 0,x/= -1,x/= -2, y/= 1,y/= 0,y/= -1,y/= -2]
main = print(makeList 50)