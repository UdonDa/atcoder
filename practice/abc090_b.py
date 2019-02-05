def solve():
    a, b = map(int, input().split())
    result = 0
    for i in range(a, b + 1):
        s = str(i)
        if s[0] == s[4] and s[1] == s[3]:
            result += 1
    print(result)


solve()
