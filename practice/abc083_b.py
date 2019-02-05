# 10進数の各桁の和の典型問題
def solve():
    n, a, b = map(int, input().split())
    s = 0
    for i in range(1, n+1):
        x = i
        m = 0
        while x:
            m += x % 10
            x //= 10
        if a <= m <= b:
            s += i
    print(s)
    
solve()