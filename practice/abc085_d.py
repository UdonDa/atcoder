# https://beta.atcoder.jp/contests/abc085/tasks/abc085_d

def solve():
    n, m = map(int, input().split())
    # n, m = 4, 1000000000
    # swing, throw = [1, 1, 1, 1], [1, 10000000, 99999999, 30000000]
    swing, throw = [], []
    for _ in range(n):
        a, b = map(int, input().split())
        swing.append(a)
        throw.append(b)
    swing = sorted(swing)
    throw = sorted(throw)
    max_swing = swing[-1]
    will_throw = [x for x in throw if x > max_swing]

    all_damage = sum(will_throw)
    answer = len(will_throw)
    if all_damage > m:
        for damage in will_throw:
            if all_damage - damage < m:
                print(answer)
                return
            else:
                all_damage -= damage
                answer -= 1
    else:
        print(answer + ((m - all_damage) + (max_swing - 1)) // max_swing)
        return

solve()