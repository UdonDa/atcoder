def solve():
    s = list(input())
    money = 700
    for x in range(3):
        if s[x] == "o":
            money += 100
    print(money)
solve()