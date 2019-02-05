N = int(input())
srimes = input().split(" ")

result = 0
before_srime = 0

# 右隣にあるものが同じかどうかを判定
for i, srime in enumerate(srimes):
    
    # if i > 1:
    # print("i : {}, srime : {}, before_srime : {}".format(i, srime, before_srime))
    if before_srime == srime:
        # print("HIT!!!!!!!!!")
        result += 1
        before_srime = int(before_srime) + 10001
        continue
    before_srime = srime

print(result)