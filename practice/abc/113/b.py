from math import fabs

def main():
  n = int(input())
  T, A = list(map(int, input().split()))
  H = list(map(int, input().split()))
  
  place = 0
  m = 1000000000
  for i, h in enumerate(H):
    t_h = T - h * 0.006
    dif = fabs(A - t_h)
    if dif < m:
      m = min(m, dif)
      place = i+1
  print(place)
main()