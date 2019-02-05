N = int(input())
li = list(map(int, input().split(" ")))

def division(li, i):
   i += 1
   li = [n / 2 for n in li]
   return li, i

i = 0
FLAG = True
while FLAG:
    if 0 in li:
        break
    for n in li:
        if n % 2 != 0:
            FLAG = False
    if FLAG:
        li, i = division(li, i)
    else:
        break
print(i)