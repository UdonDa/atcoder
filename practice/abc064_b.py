def solve():
    n = int(input())
    lists = list(map(int, input().split()))

    lists = sorted(lists)
    result = lists[-1] - lists[0]
    print(result)

solve()