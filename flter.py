def check(x):
    if(x % 2 == 0 or x %  4 == 0):
        return 1
evens = list(filter(check,range(2,30)))
print(evens)