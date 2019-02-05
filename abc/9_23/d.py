def solve():
  N, M = map(int, input().split())

  yakusuu = [i for i in range(1, M+1) if M % i == 0]
  print(len(yakusuu))

solve()