import io
import sys

_INPUT = """\
4
3 3 4 4

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------

n = int(input())
c = list(map(int, input().split()))

c.sort()

mod = 10**9 + 7
ans = 1

for i in range(n):
    ans *= c[i] - i
    ans %= mod

print(ans)
