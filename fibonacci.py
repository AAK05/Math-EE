def fibonacci(length):
    lst = [0,1]
    while len(lst) < length:
        lst.append(lst[-1]+lst[-2])
    return lst

#print(fibonacci(20))