
import io
import sys


_INPUT = """\
5 40
10 20 30 40 50

"""
sys.stdin = io.StringIO(_INPUT)


n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = "No"
for i in a:
    if i == x:
        ans = "Yes"
        pass


print(ans)
