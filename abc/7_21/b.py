s = list(input())
t = input()
counter = len(s)

FLAG = False

for i in range(counter):
  r  = ""
  for a in s:
    r += a
  if r == t:
    FLAG = True
    break
  else:
    tmp = s[0]
    s.pop(0)
    s.append(tmp)

if FLAG:
  print("Yes")
else:
  print("No")