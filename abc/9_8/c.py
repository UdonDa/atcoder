from functools import reduce

def gcds(a, b):
	while b:
		a, b = b, a % b
	return a

def gcd(*numbers):
  return reduce(gcds, numbers)

def solve():
  n, start = map(int, input().split())
  cities = input().split(" ")
  # Startを0からに変更
  cities = [int(i) - start for i in cities]
  print(abs(gcd(*cities)))

solve()