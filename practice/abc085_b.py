def solve():
    n = int(input())
    lists = [int(input()) for _ in range(n)]
    print(len(set(lists)))

solve()