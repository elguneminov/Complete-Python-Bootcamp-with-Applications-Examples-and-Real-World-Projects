def factorial(x):
    y = 1
    for i in range(1, x + 1):
        y = y * i
    return y


result = factorial(6)
print(result)
