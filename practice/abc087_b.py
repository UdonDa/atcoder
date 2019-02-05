a = int(input()) # 500円
b = int(input()) # 100円
c = int(input()) # 50円
x = int(input()) # 合計金額

result = 0

for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            re = 500 * i + 100 * j + 50 * k
            if re == x:
                result += 1
print(result)
