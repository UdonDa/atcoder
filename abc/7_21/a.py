l = list(map(int, input().split(" ")))

l = sorted(l)
cost_1 = abs(l[1] - l[0])
cost_2 = abs(l[2] - l[1])
r = cost_1 + cost_2
print(r)

