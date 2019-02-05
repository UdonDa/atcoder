# https://beta.atcoder.jp/contests/abc085/tasks/abc085_c

def solve():
    n, y = map(int, input().split())
    y = y // 1000
    for nogu in range(n+1):
        for higu in range(n + 1 - nogu):
            yuki = n - higu - nogu
            total = yuki*10 + higu*5 + nogu
            if total == y:
                print(yuki, higu, nogu)
                return
    print("-1 -1 -1")

solve()