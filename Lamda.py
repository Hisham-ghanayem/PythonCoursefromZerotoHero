def sqr(x):
    return x**2
print(sqr(10))
mynum = [1,2,3,4,5,6,7,8,9,10]
for x in map(sqr, mynum):
    print(x)
print(map(sqr, mynum))
list(map(sqr, mynum))
print(list(map(sqr, mynum)))

def slicer(names):
    if len(names) % 2== 0:
        return 'even'
    else:
        return names[1]
names = ['Hisham', 'Khalid', 'Saleh']
print(slicer(names))