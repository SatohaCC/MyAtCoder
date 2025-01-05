import io
import sys

_INPUT = """\
5 2
2 5 6 7 10

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# https://qiita.com/hyouchun/items/c2a4aa2b5ff2c177f120#%E5%95%8F%E9%A1%8C-2
#
# ---------------------------------------------------------------------------------------------------------


N, K = map(int, input().split())
A = list(map(int, input().split()))


ans = []
for i in range(N):
    if A[i] % K == 0:
        ans.append(A[i])

for i in range(len(ans)):
    print(ans[i] // K, end=" ")
