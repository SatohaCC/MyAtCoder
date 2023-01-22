import io
import sys

_INPUT = """\
3 1001
1 1
2 1
100 10

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# すごろく
# dp[i] ← アルルがマス i にたどり着くことが可能かどうか (True / False)
# 計算量は O(NM)

# ---------------------------------------------------------------------------------------------------------

N, M = map(int, input().split())

A = list(map(int, input().split()))

dp = [False] * (N + 1)

dp[0] = True

for i in range(1, N + 1):
    # print(i, end=":  ")
    for j in range(M):
        # print(A[j], end=" ")
        if i - A[j] >= 0 and dp[i - A[j]]:
            dp[i] = True
    # print()
    # print(dp)

if dp[-1]:
    print("Yes")
else:
    print("No")
