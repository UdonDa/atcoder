def solve():
  a = list(map(int, input().split()))
  # print(a)
  a = sorted(a)
  A = str(a[2]) + str(a[1])
  A = int(A)
  print(A + a[0])

solve()