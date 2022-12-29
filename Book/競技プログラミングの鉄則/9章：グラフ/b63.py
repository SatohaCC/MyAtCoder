import io
import sys

_INPUT = """\
7 8
2 2
4 5
########
#......#
#.######
#..#...#
#..##..#
##.....#
########

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 幅優先探索　最小手数(何回で移動できるかもこれで行ける)
#
# ---------------------------------------------------------------------------------------------------------

# 入力
H, W = map(int, input().split())
sx, sy = map(int, input().split())
sx -= 1
sy -= 1
gx, gy = map(int, input().split())
gx -= 1
gy -= 1

S = [input() for _ in range(H)]


INF = 1 << 61


cost = [[INF] * W for _ in range(H)]

q = []  # queue は list で再現できる

# マスに訪れる部分を関数に切り出すと良い
# cは現在のコスト
def push(x: int, y: int, c: int):
    if S[x][y] == "#":
        return
    if cost[x][y] <= c:
        return
    cost[x][y] = c
    q.append((x, y))


# 幅優先探索
push(sx, sy, 0)

for x, y in q:
    c2 = cost[x][y] + 1
    push(x - 1, y, c2)
    push(x, y - 1, c2)
    push(x + 1, y, c2)
    push(x, y + 1, c2)
print(cost[gx][gy])
