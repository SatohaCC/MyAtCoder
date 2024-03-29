import io
import sys

_INPUT = """\
3 100
1 2
5 3
10 10
"""
sys.stdin = io.StringIO(_INPUT)

# DP 横軸をそのまま～円として用いる
# Q---------------------------------------------------------------------------------------------------------
# 高橋君はN種類の硬貨をそれぞれ何枚か持っており、
# 具体的には、1≤i≤N について Ai円硬貨をBi枚持っています。
# 高橋君が現在持っている硬貨を用いて（お釣りが出ないように）ちょうど X 円を支払うことができるか判定してください。
# ---------------------------------------------------------------------------------------------------------

N, X = map(int, input().split())
A = []
for i in range(N):
    a, b = map(int, input().split())
    A.append((a, b))

INF = 9999999
dp = [[INF] * (X + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    a, b = A[i - 1]
    for j in range(X + 1):  # X円まで
        for k in range(b + 1):  # a円硬化に関してb枚まで
            if j - k * a >= 0:  # j円を超えないように。
                # １つ前[i-1]のループにk*a円プラスして、比較する
                # １つ前の段階がINFのままだと大きい数字のままなので作れない数字とわかる
                dp[i][j] = min(dp[i][j], dp[i - 1][j - k * a] + k * a)

print(dp)
if dp[N][X] == INF:
    print("No")
else:
    print("Yes")
