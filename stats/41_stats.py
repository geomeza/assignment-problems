def f(x):
    return 1/x**4

def p(x):
    return 922741.8667/x**4

def find_c(k_limit):
    output = []
    for k in range(1,k_limit):
        if k < 68:
            output.append(0)
        else:
            output.append(f(k))
    return 1/sum(output)

def find_num(percentage, lower):
    output = 0
    lower = lower
    while output < percentage:
        output += p(lower)
        lower += 1
    return lower

print(find_num(0.95, 68))


print(find_c(1000000))