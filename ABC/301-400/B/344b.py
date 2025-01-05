import io
import sys

_INPUT = """\
3
2
1
0

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------

import collections

deq = collections.deque()


while True:
    try:
        n = int(input())
        if n == 0:
            break
        deq.append(n)

    except:
        break

print(0)
while len(deq) > 0:
    print(deq.pop())
