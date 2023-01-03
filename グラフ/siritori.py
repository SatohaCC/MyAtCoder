import io
import sys

_INPUT = """\
6
apple
clang
csharp
gcc
paiza
python
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# しりとり
# https://paiza.jp/works/mondai/graph_input_problems/graph_input_problems__degree_euler_graph_boss

# 準オイラーグラフ (すべての辺を一筆書きすることができるかどうか判定してください。
# ただし、この問題では最終的に初めの頂点に戻らなくても良いものとします。
# なお、そのようなことが可能なグラフを準オイラーグラフといいます。)
# 連結な無向グラフにおいて、
# すべての辺を一筆書きすることができるための必要十分条件は以下のようになります。
# 次数が奇数である頂点の個数が、ちょうど 0 または 2 である。
# しりとりをすることができるかどうかの判定をするために、準オイラーグラフかどうかの判定をすれば良いということです。
# ---------------------------------------------------------------------------------------------------------

N = int(input())
abcd = "abcdefghijklmnopqrstuvwxyz"

G = [[0 for i in range(26)] for i in range(26)]

for i in range(N):
    s = input()
    start = abcd.index(s[0])
    end = abcd.index(s[-1])
    G[start][end] += 1
    G[end][start] += 1


Ans = 0

for i in range(26):
    # Ans.append(G[i])
    # print(sum(G[i]))
    if sum(G[i]) % 2 != 0:
        Ans += 1


if Ans in [0, 2]:
    print(1)
else:
    print(0)
