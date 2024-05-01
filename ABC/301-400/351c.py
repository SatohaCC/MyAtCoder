import io
import sys

_INPUT = """\
ab

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# https://qiita.com/hyouchun/items/c2a4aa2b5ff2c177f120#%E5%95%8F%E9%A1%8C-2
#
# ---------------------------------------------------------------------------------------------------------
S = input()

d = {}

for i in range(len(S)):
    if S[i] not in d:
        d[S[i]] = 0
    d[S[i]] += 1

ans = {}

for key, value in d.items():

    if value not in ans:
        ans[value] = 0
    ans[value] += 1

count = 0

for key, value in ans.items():
    if value == 2 or value == 0:
        continue
    else:
        count += 1

if count == 0:
    print("Yes")
else:
    print("No")
