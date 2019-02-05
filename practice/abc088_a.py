def solve():
    n = int(input())
    # 1円は1000枚まで, 500円は無限
    a = int(input())
    amari = n % 500
    if amari - a <= 0:
        print("Yes")
    else:
        print("No")
solve()