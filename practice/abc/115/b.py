def main():
  N = int(input())
  items = [int(input()) for _ in range(N)] 
  items.sort() # 最も定価が高いものを半額で変える
  items[-1] = items[-1] // 2

  result = 0
  for n in items:
    result += n
  print(result)

main()