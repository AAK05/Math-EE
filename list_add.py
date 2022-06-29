import numpy as np
def list_add(lst1,lst2,length=10000):
    length1 = len(lst1)
    length2 = len(lst2)
    while length1 < length:
        lst1.append(0)
        length1 = len(lst1)
    while length2 < length:
        lst2.append(0)
        length2 = len(lst2)
    if length1 > length:
        lst1 = lst1[0:length]
    if length2 > length:
        lst2 = lst2[0:length]
    arr1 = np.array(lst1)
    arr2 = np.array(lst2)
    arr_sum = arr1+arr2
    lst_sum = arr_sum.tolist()
    return lst_sum