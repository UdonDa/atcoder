def solve():
    n = int(input())
    tmp = n
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    if tmp % sum == 0:
        print("Yes")
    else:
        print("No")

solve()