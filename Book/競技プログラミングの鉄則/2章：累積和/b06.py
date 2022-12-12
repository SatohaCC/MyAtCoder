import io
import sys


_INPUT = """\
7
0 1 1 0 1 0 0
3
2 5
2 7
5 7
"""

sys.stdin = io.StringIO(_INPUT)


n = int(input())
# n, q = map(int, input().split())
a = list(map(int, input().split()))
q = int(input())

b = [0] * (n + 1)

for i in range(1, n + 1):
    b[i] = b[i - 1] + a[i - 1]


for _ in range(q):
    l, r = list(map(int, input().split()))
    tmp = (b[r] - b[l - 1]) * 100 / (r - l + 1)
    # 勝利回数/実行回数が50以上ならwin
    if tmp > 50:
        print("win")
    elif tmp == 50:
        print("draw")
    else:
        print("lose")
