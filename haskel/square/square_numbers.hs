squareSingles x = map(^2) (filter(<10) x)

main = print(squareSingles [2, 7, 15, 11, 5])