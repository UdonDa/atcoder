def solve():
  N, M, X, Y = map(int, input().split())
  x = list(map(int, input().split()))
  y = list(map(int, input().split()))

  x = sorted(x)
  y = sorted(y)
  
  if x[-1] < y[0]:
    # Zが存在する
    if X < y[0] <= Y:
      print('No War')
    else:
      print('War')
  else:
    print('War')


solve() 