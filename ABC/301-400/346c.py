import io
import sys

_INPUT = """\
1 3
346
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# https://qiita.com/hyouchun/items/c2a4aa2b5ff2c177f120#%E5%95%8F%E9%A1%8C-2
#
# ---------------------------------------------------------------------------------------------------------

N, K = map(int, input().split())
A = list(map(int, input().split()))

gray = set()

for a in A:
    if  a <= K:
        gray.add(a)

ans = K * (K + 1) // 2 - sum(gray)

print(ans)
