def solve():
    k, s = map(int, input().split())
    # 0<= x, y, z <= K
    # x + y + z = s
    a = [0 for x in range(k+1) for y in range(k+1) for z in range(k+1) if (x+y+z)==s]
    print(len(a))
solve()