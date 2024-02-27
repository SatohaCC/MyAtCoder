import io
import sys

_INPUT = """\
4
16 9 24 9
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 偶数+偶数　か　奇数+奇数　の２パターン
# 偶数が１つしかない場合は奇数+奇数のように個数が少ない場合のif文も用意する
# ---------------------------------------------------------------------------------------------------------

N = int(input())
A = list(map(int, input().split()))
even = []
odd = []

for i in range(N):
    if A[i] % 2 == 0:
        even.append(A[i])
    else:
        odd.append(A[i])


c = sorted(even)
d = sorted(odd)

if len(c) > 1 and len(d) > 1:
    if c[-1] + c[-2] >= d[-1] + d[-2]:
        print(c[-1] + c[-2])
    else:
        print(d[-1] + d[-2])
elif len(c) > 1 and len(d) <= 1:
    print(c[-1] + c[-2])

elif len(d) > 1 and len(c) <= 1:
    print(d[-1] + d[-2])


else:
    print(-1)
