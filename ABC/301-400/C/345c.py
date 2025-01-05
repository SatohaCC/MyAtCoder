import io
import sys

_INPUT = """\
abc


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
# +
# ---------------------------------------------------------------------------------------------------------

S = list(map(str, input()))
N = len(S)

d = dict()
for i in range(N):
    if S[i] in d:
        d[S[i]] += 1
    else:
        d[S[i]] = 1

ans = 0

is_duplicate = False
for count in d.values():
    if count >= 2:
        ans += count * (count - 1) // 2
        is_duplicate = True

ALL = N * (N - 1) // 2

ans = ALL - ans 

if is_duplicate:
    ans  += 1

print(ans)
