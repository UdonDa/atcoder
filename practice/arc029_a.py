# https://arc029.contest.atcoder.jp/tasks/arc029_1
N = int(input())
time = [int(input()) for _ in range(N)]

# A, Bに乗せる組み合わせをビットの状態で調べる -> bit全探索
def solve():
    answer = 10000

    for i in range(2 ** N):
        table_a, table_b, t = 0, 0, i
        for j in range(N):
            if t & 1 == 1:
                table_a += time[j]
            else:
                table_b += time[j]
            t >>= 1
        answer = min(answer, max(table_a, table_b))
    print(answer)

solve()
