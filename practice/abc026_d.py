# https://abc026.contest.atcoder.jp/tasks/abc026_d
# ２分探索

import math


def solve():
    a, b, c = map(int, input().split())
    ft, low, high = 100, 0, 500
    calc = lambda t: a * t + b * math.sin(c * t * math.pi)
    for i in range(100):
        mid = (low + high) / 2
        if calc(mid) < ft:
            low = mid
        else:
            high = mid
    print(low)
solve()