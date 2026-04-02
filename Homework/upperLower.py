s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
mylist = list(s)
def up_low(mylist):
    low = 0
    high = 0
    for ch in mylist:
        if ch.isupper():
            high += 1

        elif ch.islower():
            low += 1
    return f'Number of Upper characters :{high} \nNumber of Upper characters :{low}'
print (up_low(mylist))