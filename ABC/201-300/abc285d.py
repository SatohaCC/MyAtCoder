import io
import sys

_INPUT = """\
5
aaa bbb
yyy zzz
ccc ddd
xxx bbb
bbb ccc


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------
N = int(input())
M = N * 2
R = []
indegree = [0 for _ in range(M)]
outdegree = [0 for _ in range(M)]

d = {}

for i in range(N):
    a, b = input().split()
    if a not in d:

        d[a] = len(d)

    if b not in d:
        d[b] = len(d)
    indegree[d[a]] += 1
    outdegree[d[b]] += 1
    R.append(b)


ans = True
for i in range(len(d)):
    if indegree[i] == outdegree[i]:
        ans = True
    else:
        ans = False
        break

if ans:
    print("No")
else:
    print("Yes")
