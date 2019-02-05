from math import fabs


def main():
  S = list(input())
  result = 1000
  target = 753
  for i in range(len(S) - 2):
    s = int(S[i] + S[i+1] + S[i+2])
    s = int(fabs(target - s))
    result = min(s, result)
  print(result)

main()