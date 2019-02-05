def solve():
    n = int(input())
    cards = list(map(int, input().split()))
    cards = sorted(cards, reverse=True)
    alice, bob = 0, 0
    for i in range(len(cards)):
        if i % 2 == 0:
            alice += cards[i]
        else:
            bob += cards[i]
    print(alice - bob)


solve()