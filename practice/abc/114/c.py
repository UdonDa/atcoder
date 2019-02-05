from itertools import product

def main():
  N = int(input())

  results = list()
  ans = 0

  for i in range(1, 10):
    for j in list(product(['3', '5', '7'], repeat=i)):
      results.append(''.join(map(str, list(j))))

  for result in results:
    if int(result) > N:
      break
    if '3' in result and '5' in result and '7' in result:
      ans +=1

  print(ans)


main()