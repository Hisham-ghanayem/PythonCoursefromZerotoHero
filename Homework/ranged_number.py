def ran_check(num, low, high):
    if low < num < high:
        return f'{num} is in the range between {low} and {high}'
    else:
        return f'{num} is not in the range between {low} and {high}'
print (ran_check(30, 10, 20))

