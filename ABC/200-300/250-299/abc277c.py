import io
import sys

_INPUT = """\
4
1 4
4 3
4 10
8 3


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# はしごを辺だと思ってBFS
# 最大到達を求める
# ---------------------------------------------------------------------------------------------------------

from collections import deque

# 再帰呼び出しの深さの上限を 120000 に設定
import sys

sys.setrecursionlimit(120000)


N = int(input())

# 隣接辞書の作成
from collections import defaultdict

G = defaultdict(list)
# defaultdict(<class 'list'>, {1: [4], 4: [1, 3, 10], 3: [4, 8], 10: [4], 8: [3]})

for i in range(N):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


# Sに到達階層を記録する
S = {1}

# Qに探索する階層を一時保持
Q = deque()
# １階からスタートする
Q.append(1)

while len(Q) >= 1:
    # posが現在の階層
    pos = Q.popleft()
    # G[pos]が梯子がかかっている階層
    for nex in G[pos]:
        if not nex in S:
            # 梯子を１個づつ確認して、Sに記録していなければ追加
            S.add(nex)
            # その到達階の梯子も調べる必要があるのでQに追加
            Q.append(nex)


print(max(S))
