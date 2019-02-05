# def gcd(a, b):
# 	while b:
# 		a, b = b, a % b
# 	return a

# def lcm(a, b):
# 	return a * b // gcd (a, b)

# def f(m, input):
#   r = 0
#   for i in input:
#     r += m % i
#   return r

N = map(int, input())
a_n = list(map(int, input().split(" ")))
# a_n = sorted(a_n)

max = 0
for x in a_n:
  max += x
 
# result = []
# for m in range(max):
  # out = f(m, a_n)
  # result.append(out)
# re = sorted(result)
#print(re[-1])
#print(max) #994 518 941 851 647 2 581 -> 4534
print(max - len(a_n))