# N = int(input())

# inputs = [input().split(" ") for _ in range(N)]    


# for input in inputs:
#     # print(input)
#     A = int(input[0])
#     B = int(input[1])
#     C = int(input[2])
#     D = int(input[3])
#     FLAG = True
#     asa = A
#     count = 0
#     start_roop = 0
#     while FLAG:
#         yoru = asa - B
#         # print("yoru : {}. start_roop : {}".format(yoru, start_roop))



#         if yoru != start_roop:
#             if yoru < 0:
#                 print("No")
#                 FLAG = False
#                 break
#             elif yoru <= C:
#                 count += 1
#                 yoru += D
#                 start_roop = yoru
#                 if count > 100:
#                     print("Yes")
#                     break
#             elif yoru > C:
#         else:
#             print("Yes")

#         if 

import fractions

def judge(A, B, C, D):
    if A < B: # 買えない
        return False
    if D < B: # 補充が間に合わないのでいつか無くなる
        return False
    if B <= C: # 補充間に合う状況で、必ず０個以上の在庫がある
        return True
    G = fractions.gcd(B, D)
    R = A % G
    if (C + G - R - B) < 0: # C + G - R = 在庫の最小数
        return False
    else:
        return True

T = int(input())
data = []
for _ in range(T):
    data.append(int(xi) for xi in input().split())
for A, B, C, D in data:
    print("Yes") if judge(A, B, C, D) else print("No")


