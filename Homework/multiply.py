x = [1, 2, 3, -4]

def multiply(x):
    result = 1
    for number in x:
        result *= number
    return result

print(multiply(x))
