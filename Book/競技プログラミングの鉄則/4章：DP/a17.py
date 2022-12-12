# 最短時間で移動する方法(ルートの調べ方、DPから逆算)

import io
import sys

_INPUT = """\
5
2 4 1 3
5 3 3
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------

K = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0] * (K + 1)
dp[1] = 0
dp[2] = A[0]

for i in range(3, K + 1):
    dp[i] = min(dp[i - 1] + A[i - 2], dp[i - 2] + B[i - 3])

ans = []
place = K

while True:
    ans.append(place)
    if place == 1:
        break

    if dp[place - 1] + A[place - 2] == dp[place]:
        place -= 1
    else:
        place -= 2

print(len(ans))
print(*ans[::-1])
