def solve():
  a, b = map(int, input().split())
  d = a * b
  if d % 2 == 0:
    print('No')
  else:
    print('Yes')

solve()