def solve():
    s = input()
    s = set(s)
    dic = set(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
    s = sorted(list(dic - s))
    if len(s) == 0:
        print("None")
        return
    print(s[0])


solve()