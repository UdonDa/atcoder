def solve():
    n, m = map(int, input().split())
    lists = []

    for _ in range(m):
        lists += input().split()
    
    for i in range(1, n + 1):
        print(lists.count(str(i)))


solve()