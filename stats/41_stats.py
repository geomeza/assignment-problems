def f(x):
    return 1/x**5

def find_c(k_limit):
    output = []
    for k in range(1,k_limit):
        if k < 25:
            output.append(0)
        else:
            output.append(f(k))
    return 1/sum(output)

print(find_c(1000000))