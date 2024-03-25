import io
import sys

_INPUT = """\
3 2



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------

W, B = map(int, input().split())

S_init = "wbwbwwbwbwbw"
S_size = len(S_init)
S = S_init * 20

for i in range(12):
    T = S[i : i + W + B]
    if T.count("w") == W:
        if T.count("b") == B:
            print("Yes")
            exit()

print("No")
