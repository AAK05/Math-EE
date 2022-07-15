from mpmath import mp

def divide(num1,num2,dp=10000):
    f = num2//(10*num1) + 3
    mp.dps = dp+f
    ans = mp.fdiv(num1,num2)
    ans_str = str(ans)
    ans_lst = []
    index = ans_str.find(".")
    for char in ans_str:
        if char == ".":
            continue
        ans_lst.append(int(char))
    ans_lst = ans_lst[index:]
    while len(ans_lst) <= dp:
        ans_lst.append(0)
    return ans_lst[:dp]

if __name__ == "__main__":
    print(divide(80,7,20))