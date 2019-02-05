def solve():
    n, l = map(int, input().split())
    lists = [input() for _ in range(n)]
    # for _ in range(l):
    #     lists.append(input())
    lists = sorted(lists)
    for s in lists:
        print(s, end="")
    


solve()