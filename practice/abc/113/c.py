# def main():
#   # N個の県，M個の市，
#   # 市iが誕生したのはY_i年で県P_iに属す
#   # 市iが県P_iの中でx番目にできた市だと、市iの認識番号の上6桁はP_i,下6桁はx
#   # 6桁以下だと6桁になるように左に0詰める

#   N, M = map(int, input().split())
#   iPY = []
#   for i in range(M):
#     p, y = map(int, input().split())
#     iPY.append([i, p, y])
#   # PY = [list(map(int, input().split())) for _ in range(M)]
#   iPY_sorted = sorted(iPY, key=lambda x: x[2])

#   city_count = {}
#   order = {}
#   for i, p, y in iPY_sorted:
#     if not p in city_count:
#       city_count[p] = 0
#     city_count[p] += 1
#     order[p, i] = city_count[p]
    
#   for i, p, y in enumerate(iPY):
#     print('{:06}{:06}'.format(p, order[p, i]))

# main()


N, M = map(int, input().split())
iPY = []
 
for i in range(M):
    p, y = map(int, input().split())
    iPY.append([i, p, y])
 
city_count = {}
order = {}
 
for i, p, y in sorted(iPY, key=lambda x: x[2]):
    if not p in city_count:
        city_count[p] = 0
    city_count[p] += 1
    order[p, i] = city_count[p]
    
for i, p, y in iPY:
    print('{:06}{:06}'.format(p, order[p, i]))