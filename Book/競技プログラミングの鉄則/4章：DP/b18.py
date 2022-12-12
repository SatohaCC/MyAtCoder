import io
import sys

_INPUT = """\
10 100
14 23 18 7 11 23 23 5 8 2

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# DP　復元
# 部分和
# ---------------------------------------------------------------------------------------------------------

N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False for _ in range(S + 1)] for _ in range(N + 1)]


dp[0][0] = True


for i in range(1, N + 1):
    for j in range(0, S + 1):

        if j < A[i - 1]:
            if dp[i - 1][j]:
                dp[i][j] = True

        if j >= A[i - 1]:
            if dp[i - 1][j] or dp[i - 1][j - A[i - 1]]:
                dp[i][j] = True

if dp[N][S] == False:
    print("-1")
    exit()

Ans = []

place = S

for i in reversed(range(1, N + 1)):
    if dp[i - 1][place]:
        place = place - 0
    else:
        place = place - A[i - 1]
        Ans.append(i)

Ans.reverse()
print(len(Ans))
print(*Ans)
