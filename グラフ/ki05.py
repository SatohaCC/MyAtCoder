import io
import sys

_INPUT = """\
7
2 3
3 4
3 1
1 7
1 5
5 6
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 木の中心 (paizaランク B 相当)
# 「その頂点が葉である」→ 「その頂点に接続する辺が１本である」に言い換える
# 木には図にした際に、一番外側となる葉と呼ばれる頂点が必ず存在します。
# 辺の削除は、木の情報を持つ隣接リストから削除された辺で隣接していた頂点を削除したり、
# 隣接行列の辺で隣接していた頂点の値を 1 → 0 に修正することで行うことができます。
# 頂点の削除は、木から取り除かれた（次数が 0 になった）頂点番号を記憶しておくことで行うことができます。
# ---------------------------------------------------------------------------------------------------------

N = int(input())
# N, X, Y = map(int, input().split())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# A = [int(input()) for _ in range(N)]

G = [[0 for i in range(N)] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1][b - 1] = 1
    G[b - 1][a - 1] = 1


num_of_vertex = N

# 存在している頂点
exist = [1] * N

while num_of_vertex > 2:
    for i in range(N):
        cnt = 0
        for j in range(N):
            if G[i][j] == 1:
                cnt += 1
        if cnt == 1:
            # cnt が1とは頂点ということ。G[i]をすべて0で初期化
            num_of_vertex -= 1
            exist[i] = 0
            G[i] = [0] * N

    # i側は初期化したのでjを初期化したい
    for i in range(N):
        for j in range(N):
            if exist[j] == 0 and G[i][j] == 1:
                G[i][j] = 0

for i in range(N):
    if exist[i] == 1:
        print(i + 1)
