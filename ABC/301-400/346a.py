import io
import sys

_INPUT = """\
5
22 75 26 45 72

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------

N = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(1, N):
    ans.append(A[i - 1] * A[i])
print(*ans)
