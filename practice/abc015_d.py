# https://abc015.contest.atcoder.jp/tasks/abc015_4

def solve():
    w = int(input())
    n, k = map(int, input().split())
    width, importance = [], []

    for _ in range(n):
        a, b = map(int, input().split())
        width.append(a)
        importance.append(b)
    
    dp = [[0 for _ in range(w + 1)] for _ in range(k + 1)]
    
    for i in range(n):
        for j in range(w, 0, -1):
            for l in range(1, k):
              if dp[l][j] > 0 and j + width[i] <= w:
                  dp[l + 1][j + width[i]] = max(dp[l + 1][j + width[i]], dp[l][j] + importance[i])
        if width[i] <= w:
            dp[l][width[i]] = max(dp[l][width[i]], importance[i])
    print(max([max(dp[i]) for i in range(1, k + 1)]))

solve()

