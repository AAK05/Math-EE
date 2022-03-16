def primes(length):
    if length==0:
        return []
    if length==1:
        return [2]
    lst = [2,3]
    num = 5
    while len(lst) < length:
        isprime = True
        for i in range(2,num//2):
            if num%i==0:
                isprime = False
                break
        if isprime == True:
            lst.append(num)
        num+=1
    return lst

#print(primes(20))