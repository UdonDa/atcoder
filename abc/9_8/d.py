def solve():
  h, w = map(int, input().split())
  table = []
  for _ in range(h):
    table.append(list(map(int, input().split())))
  
  
  count = 0
  result = []

  for i in range(h):
    j = 0
    while j < w:
      if table[i][j] % 2 != 0:
        s = j
        j += 1
        while j < w:
          if table[i][j] % 2 != 0 or j == w - 1:
            table[i][s] -=1
            table[i][j] += 1
            for k in range(s, j):
              count += 1
              result.append(((i, k), (i, k + 1)))
            break
          j += 1
      j += 1
  i = 0
  while i < h:
    if table[i][-1] % 2 != 0:
      s = i
      i += 1
      while i < h:
        if table[i][-1] % 2 != 0 or i == h - 1:
          for k in range(s, i):
            count += 1
            result.append(((k, w-1), (k+1, w-1)))
          break
        i += 1
    i += 1
  print(count)
  for e in result:
    print(e[0][0] + 1, e[0][1] + 1, e[1][0] + 1, e[1][1]+ 1)



solve()




# def solve():
#   # まだ選んだことないます農地一枚以上コインが置かれているマスを１つ選び、そのマスに置かれているコインのうち一枚を上下左右に隣接するいずれかのマスに移動する
#   h, w = map(int, input().split())
#   table = []

#   # テーブル作成
#   for _ in range(h):
#     a = input().split(" ")
#     table.append(a)
  
#   # print(table)

#   H = len(table) - 1
#   W = len(table[0]) - 1
#   tmp_table = []
#   for i in range(h):
#     for j in range(w): 
#       table[i][j] = int(table[i][j]) % 2
#   print(table)
#       # ue = 0
#       # sita = 0
#       # migi = 0
#       # hidari = 0

#       # if i == 0 and j == 0:
#       #   # 左上
#       #   # print("左上")
#       #   migi = tmp_table[i][j+1]
#       #   sita = tmp_table[i+1][j]

#       # elif i == 0 and j == W:
#       #   # 右上
#       #   print("右上")
#       #   sita = tmp_table[i+1][j]
#       #   hidari = tmp_table[i][j-1]

#       # elif i == H and j == 0:
#       #   # 左下
#       #   print("左下")
#       #   migi = tmp_table[i][j+1]
#       #   ue = tmp_table[i-1][j]

#       # elif i == H and j == W:
#       #   # 右下
#       #   print("右下")
#       #   hidari = tmp_table[i][j-1]
#       #   ue = tmp_table[i-1][j]

#       # elif i == 0:
#       #   # 上側
#       #   print("上側")
#       #   sita = tmp_table[i+1][j]
#       #   hidari = tmp_table[i][j-1]
#       #   migi = tmp_table[i][j+1]
#       # elif i == H:
#       #   # 下側
#       #   print("下側")
#       #   ue = tmp_table[i-1][j]
#       #   hidari = tmp_table[i][j-1]
#       #   migi = tmp_table[i][j+1]
#       # elif j == 0:
#       #   # 左側
#       #   print("左側")
#       #   ue = tmp_table[i-1][j]
#       #   sita = tmp_table[i+1][j]
#       #   migi = tmp_table[i][j+1]

#       # elif j == W:
#       #   # 右側
#       #   print("右側")
#       #   ue = tmp_table[i-1][j]
#       #   sita = tmp_table[i+1][j]
#       #   hidari = tmp_table[i][j-1]


      


  
# solve()