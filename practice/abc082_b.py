def solve():
    s = input()
    t = input()

    s = sorted(s)
    t = sorted(t, reverse=True)
    print(s, t)
    print("".join(s), "".join(t))
    if "".join(s) < "".join(t):
        print("Yes")
    else:
        print("No")
solve()