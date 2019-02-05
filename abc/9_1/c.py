def solve():
  n, k = map(int, input().split())
  ans = 0
  if k % 2 == 1:
    ans = (n // k) ** 3
  else:
    full, half = [], []
    for i in range(int(k/2), n+1, int(k/2)):
      if i % k == 0:
        full.append(i)
      else:
        half.append(i)
    
    ans = len(half) ** 3 + len(full) ** 3
  
  print(ans)


solve()




# from itertools import product

# def solve():
#   n, k = map(int, input().split())
#   count = 0
#   # # A解法
#   # for a in range(1, n+1):
#   #   for b in range(1, n+1):
#   #     # for c in range(1, n+1):
#   #     count += min(a, cal(a, b, 3, n, k))

#   # B解法
#   ary = [(a, b, c)
#     for a in range(1, n+1)
#     for b in range(1, n+1)
#     for c in range(1, n+1)]
#   print(ary)

#   # for i in range(len(ary)):
#   #   A = ary[i][0] + ary[i][1]
#   #   B = ary[i][1] + ary[i][2]
#   #   C = ary[i][0] + ary[i][2]

#   #   if A%k ==0 and B%k ==0 and C%k ==0:
#   #     count += 1


  
#   # for a, b, c in ary:
#   #   if (a+b)%k == 0 and (b+c)%k == 0 and (c+a)%k == 0:
#   #     count += 1

#   # C解法
#   # a = range(1, n+1)
#   # for i in range(1, n+1):
#   #   b = i


  
#   # print(count)


# solve()
