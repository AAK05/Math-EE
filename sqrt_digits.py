from mpmath import mp

def square_rt(number,dp=10000):
    mp.dps = dp + 3
    ans = mp.sqrt(number)
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

def scalar_mult(data,factor):
    output = []
    for i in data:
        output.append((i*factor)%10)
    return output

def write_json(data,fname):
    import json
    with open(fname,"w") as f:
        json.dump(data,f)

def write_sqrt(number,dp=10000):
    import json
    data = square_rt(number,dp)
    fname = "sqrt-{}-{}dp.json".format(number,dp)
    with open(fname,"w") as f:
        json.dump(data,f)

if __name__ == "__main__":
    #print(square_rt(2,1000))
    #write_sqrt(2,1000000)
    write_json(scalar_mult(square_rt(2,1000000),3),"sqrt-2-factor3.json")