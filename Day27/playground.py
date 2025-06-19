def add(*args):
    total = 0
    for n in args:
        total += n
    return total
     
addon = add(2,3,4,5)
print(addon)