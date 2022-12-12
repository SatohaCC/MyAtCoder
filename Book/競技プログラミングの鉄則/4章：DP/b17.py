import io
import sys

_INPUT = """\
6
30 10 60 10 60 50

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------

N = int(input())
h = list(map(int, input().split()))


dp = [0] * (N + 1)
dp[1] = 0
dp[2] = abs(h[1] - h[0])

for i in range(3, N + 1):
    dp[i] = min(
        dp[i - 1] + abs(h[i - 1] - h[i - 2]), dp[i - 2] + abs(h[i - 1] - h[i - 3])
    )

# print(dp)

ans = []
place = N

while True:
    ans.append(place)
    if place == 1:
        break

    if dp[place] == dp[place - 1] + abs(h[place - 1] - h[place - 2]):
        place -= 1
    else:
        place -= 2


print(len(ans))
print(*ans[::-1])
