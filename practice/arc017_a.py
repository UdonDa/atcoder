import math

def solve():
    n = int(input())
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print("NO")
            return
    print("YES")
  
solve()
