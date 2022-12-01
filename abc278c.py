import io
import sys

_INPUT = """\
20 40

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------

h, m = map(int, input().split())


def check(h, m):
    str_h = "0" + str(h)
    str_m = "0" + str(m)
    change_h = str_h[-2] + str_m[-2]
    change_m = str_h[-1] + str_m[-1]
    return int(change_h), int(change_m)


time_list = []
for i in range(24):
    for j in range(60):
        time_list.append([i, j])

while True:
    a, b = check(h, m)
    if [a, b] in time_list:
        print(*[h, m])
        break
    else:
        m += 1
        if m == 60:
            h += 1
            m = 0
            if h == 24:
                h = 0
