import io
import sys

_INPUT = """\
3
500000000 600000000
600000000 700000000
700000000 800000000
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#はしごを辺だと思ってBFS/DFSかUnion-Findでどこまで登れるか調べる　グラフは辞書で持てばいい
#
# ---------------------------------------------------------------------------------------------------------
N = int(input())

q = [None] * N
for i in range(N):
    a = list(map(int, input().split()))
    q[i] = a

end = [1]
for i in range(N):
    if q[i][0] in end or q[i][1] in end:
        end.append(q[i][1])
        end.append(q[i][0])


print(max(end))
