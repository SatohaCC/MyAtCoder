import io
import sys

_INPUT = """\
7
478 369 466 343 541 42 165
20
2 1
1 7 729
1 6 61
1 6 838
1 3 319
1 4 317
2 4
1 1 673
1 3 176
1 5 250
1 1 468
2 6
1 7 478
1 5 595
2 6
1 6 599
1 6 505
2 3
2 5
2 1

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

query = [None] * Q

for i in range(Q):
    x = list(map(int, input().split()))
    query[i] = x

for i in range(Q):
    # print(query[i])
    if query[i][0] == 1:
        A[query[i][1] - 1] = query[i][2]
        # print()
    else:
        print(A[query[i][1] - 1])
