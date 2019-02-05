from math import sqrt

def cal_euclidean(a, b):
    a_x, a_y = a[0], a[1]
    b_x, b_y = b[0], b[1]

    euclidean = sqrt((a_x - b_x) ** 2 + (a_y - b_y) ** 2)
    return euclidean


def solve():
    n = int(input())
    co = []
    for _ in range(n):
        x, y = map(int, input().split())
        co.append([x, y])
    # 2重内包表記
    a = [cal_euclidean(a, b) for i, a in enumerate(co) for b in co[i+1:]]
    a = sorted(a)
    print(a[-1])
            
solve()