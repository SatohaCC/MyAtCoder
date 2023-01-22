import io
import sys

_INPUT = """\
8 1000000000 1000000000
bcdfcgaa


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# https://atcoder.jp/contests/abc286/tasks/abc286_c
# 回分つくれるかの判定
# ---------------------------------------------------------------------------------------------------------
n, a, b = map(int, input().split())
s = input()
# 文字列を足して移動させた分も配列にしておく
s += s

ans = 1 << 60
for i in range(n):
    # A円払うパターンを全探索する
    tmp = a * i
    for j in range(n // 2):
        # print(i + j, "       ", i + n - 1 - j)
        if s[i + j] != s[i + n - 1 - j]:
            tmp += b
    ans = min(ans, tmp)
print(ans)
