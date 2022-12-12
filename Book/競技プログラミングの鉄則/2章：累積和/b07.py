# １次元の累積和
# 配列の長さに注意
# 終わりの処理がA問題と違う。図解すると分かりやすい

import io
import sys

_INPUT = """\
10
7
0 3
2 4
1 3
0 3
5 6
5 6
5 6
"""
sys.stdin = io.StringIO(_INPUT)

T = int(input())
N = int(input())

# employee :従業員
employee = [0] * (T + 1)
for _ in range(N):
    L, R = map(int, input().split())
    employee[L + 1] += 1
    employee[R + 1] -= 1

# print(employee)

ans = [0] * (T + 1)
for i in range(1, T + 1):
    ans[i] = ans[i - 1] + employee[i]
    print(ans[i])
