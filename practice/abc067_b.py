def solve():
    n, k = map(int, input().split())
    lists = list(map(int, input().split()))
    lists = sorted(lists, reverse=True)
    result = 0
    for i in range(k):
        result += lists[i]
    print(result)


solve()