def solve():
  S = list(input())
  T = list(input())

  s = set(S)
  t = set(T)
  print(s)
  print(t)
  if s == t:
    print('Yes')
  else:
    print('No')



solve()