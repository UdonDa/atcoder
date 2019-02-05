# https://abc007.contest.atcoder.jp/tasks/abc007_3

from collections import deque


def solve():
    r, c = map(int, input().split())
    # 位置を0から始めるため
    f = lambda e: int(e) - 1
    sy, sx = map(f, input().split())
    gy, gx = map(f, input().split())
    table = [[e for e in input()] for _ in range(r)]

    # answer table
    ans_table = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if table[i][j] == ".":
                ans_table[i][j] = 500000
            else:
                ans_table[i][j] = -1
    ans_table[sy][sx] = 0

    isAppended = lambda x, y, cn: 0 <= x <= c-1 and 0 <= y <= r-1 \
                    and table[y][x] == "." and (cn + 1) < ans_table[y][x]
    mx = [1, -1, 0, 0]
    my = [0, 0, 1, -1]

    q = deque([(sx, sy, 0)])
    while q:
        cx, cy, cnt = q.pop()
        for i in range(4):
            x, y = cx + mx[i], cy + my[i]
            if isAppended(x, y, cnt):
                q.append((x, y, cnt+1))
    print(ans_table[gy][gx])

    