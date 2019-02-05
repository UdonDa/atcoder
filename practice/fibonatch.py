import time

def solve(n):
    if n <= 1:
        return 1
    else:
        return solve(n-1) + solve(n-2)

num = dict()
def top_down(n):
    print("___ : ", n)
    if n <= 1:
        return 1
    else:
        if n in num:
            print("b")
            return num[n]
        else:
            # print(top_down(n-1))
            print("a")
            num[str(n)] = top_down(n-1) + top_down(n-2)





print(top_down(5))


# a = dict()
# a["5"] = 5
# print(type(a["5"]))