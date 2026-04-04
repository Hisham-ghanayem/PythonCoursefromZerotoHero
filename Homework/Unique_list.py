x = [1,1,1,2,3,4,5,5,6,6,6,7,10]

def unique_list(x):
    return list(dict.fromkeys(x))
print(unique_list(x))
