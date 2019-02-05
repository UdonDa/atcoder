def main():
  N, K = map(int, input().split(' '))
  # N本の木があって，i本目の木はh_i[m]
  # K本選んで電飾する.
  # 木の内一番高いのをh_max[m], 低いものをh_min[m]
  # min(h_max - h_min)をしたい.
  trees = [int(input()) for _ in range(N)]
  trees.sort()
  trees = [n - trees[0] for n in trees]
  # print(trees[K-1] - trees[0]) -> これだと，最初の方はかなり分散が大きい配列で，後ろの方が分散が小さい配列だとダメ
  # 例[0, 100, 101, 102] から2個選ぶ時, 上記だと100が帰ってくる.
  # MIN = 100000000000000
  # print(trees)
  # for n in range(K): -> 計算量削減する必要がある.
  # for n in range(N - K + 1):
  #   t = trees[n+K-1] - trees[n]
  #   MIN = min(t, MIN)
  MIN = min([trees[n+K-1] - trees[n] for n in range(N-K+1)])
  print(MIN)

main()