import io
import sys

_INPUT = """\
10
eixfumagit
vtophbepfe
pxbfgsqcug
ugpugtsxzq
bvfhxyehfk
uqyfwtmglr
jaitenfqiq
acwvufpfvv
jhaddglpva
aacxsyqvoj
eixfumagit
vtophbepfe
pxbfgsqcug
ugpugtsxzq
bvfhxyehok
uqyfwtmglr
jaitenfqiq
acwvufpfvv
jhaddglpva
aacxsyqvoj

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# https://qiita.com/hyouchun/items/c2a4aa2b5ff2c177f120#%E5%95%8F%E9%A1%8C-2
#
# ---------------------------------------------------------------------------------------------------------
N = int(input())
A = [input() for _ in range(N)]
B = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if A[i][j] != B[i][j]:
            print(i + 1, j + 1)
