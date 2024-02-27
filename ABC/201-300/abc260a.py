import io
import sys

_INPUT = """\
jfi



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 辞書のValueで検索
#
# ---------------------------------------------------------------------------------------------------------


s = input()
d = {}
for i in range(3):
    if s[i] not in d:
        d[s[i]] = 0
    d[s[i]] += 1

if len(d) == 1:
    print(-1)
    exit()

# 辞書のValueで検索　リストで返却される
keys = [key for key, value in d.items() if value == 1]
print(*keys[0])
