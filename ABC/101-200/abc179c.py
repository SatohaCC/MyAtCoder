import io
import sys

_INPUT = """\
100


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------

n = int(input())
ans = 0
for i in range(1, n):
    ans += (n - 1) // i
print(ans)
