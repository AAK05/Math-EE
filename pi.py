def pi(length):
    from mpmath import mp
    lst=[]
    mp.dps=length+1#Finds the length of pi to 1 more than necessary
    #Done so that rounding errors are not affecting the output
    #Credit to the developer(s) at mpmath
    pistring = str(mp.pi)
    pistring = pistring[0]+pistring[2:]
    for digit in pistring:
        lst.append(int(digit))
    return lst[0:-1] #This is done to shorten by 1

#print(pi(20))