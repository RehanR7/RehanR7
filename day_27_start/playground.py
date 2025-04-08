def add(*args):
    sum = 0
    for item in args:
        sum += item
    return sum

print(add(4,5,6,6,5,43))