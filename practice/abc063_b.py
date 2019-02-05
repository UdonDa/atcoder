def solve():
    s = list(input())
    len_bf = len(s)
    len_af = len(set(s))

    if len_bf == len_af:
        print("yes")
    else:
        print("no")

solve()