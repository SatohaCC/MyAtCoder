import io
import sys

_INPUT = """\
11
3 1 4 1 5 9 2 6 5 3 5

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 数え上げ
#
# ---------------------------------------------------------------------------------------------------------

N = int(input())

A = list(map(int, input().split()))

ans = {}

for i in range(N):
    # 初登場は０で初期化
    if A[i] not in ans:
        ans[A[i]] = 0
    # 毎回+１する
    ans[A[i]] += 1

print(len(ans))