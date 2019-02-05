# https://beta.atcoder.jp/contests/abc108/tasks/abc108_a

def solve():
  x = int(input())
  count = 0

  for i in reversed(range(x)):
    i += 1

    if i % 2 ==0:
      count += i / 2
    else:
      count += i // 2
      
  
  print(int(count))

solve()