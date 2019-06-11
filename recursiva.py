def fibonach(x):
    if x == 1 or x == 0:
        return x
    else:
        return fibonach(x-1) +  fibonach(x-2)

x = int(input('Digite para saber a sequencia'))

print(fibonach(x))
