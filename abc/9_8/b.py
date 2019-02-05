def solve():
  n = int(input())
  words = []

  for _ in range(n):
    word = input()
    words.append(word)
  set_word = set(words)
  if len(set_word) != len(words):
    print("No")
    return 0

  for i, word in enumerate(words):
    if i > 0:
      last = words[i-1][-1]
      front = words[i][0]

      if front != last:
        print("No")
        return 0
      

  print("Yes")



solve()