def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def lcm(a, b):
	return a * b // gcd (a, b)

def solve():
    n = int(input())
    clocks = [int(input()) for _ in range(n)]
    ans = clocks[0]
    for i in clocks[1:]:
        ans = lcm(ans, i)
    print(ans)

solve()