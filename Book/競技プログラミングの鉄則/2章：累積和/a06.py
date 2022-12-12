import io
import sys

_INPUT = """\
10 5
8 6 9 1 2 1 10 100 1000 10000
2 3
1 4
3 9
6 8
1 10

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 累積和　cumulative
# 区間の合計を求める
# ---------------------------------------------------------------------------------------------------------

N, Q = map(int, input().split())
A = list(map(int, input().split()))

cumulative = [0 for _ in range(N + 1)]
cumulative[1] = A[0]

for i in range(1, N + 1):
    cumulative[i] = cumulative[i - 1] + A[i - 1]


for i in range(Q):
    l, r = map(int, input().split())
    print(cumulative[r] - cumulative[l - 1])
