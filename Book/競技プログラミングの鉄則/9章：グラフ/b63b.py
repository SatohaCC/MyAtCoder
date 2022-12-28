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
# 幅優先探索　最小手数
#
# ---------------------------------------------------------------------------------------------------------


from collections import deque

H, W = map(int, input().split())
sx, sy = map(int, input().split())
sx -= 1
sy -= 1
gx, gy = map(int, input().split())
gx -= 1
gy -= 1

G = [input() for _ in range(H)]


INF = 1 << 61
# 幅優先探索の初期化
cost = [[INF] * W for _ in range(H)]
# キューの用意とスタート地点の追加＆初期値を０
Q = deque()
Q.append((sx, sy))

cost[sx][sy] = 0

# マスに訪れる部分を関数に切り出すと良い
# cは現在のコスト
def push(x: int, y: int, c: int):
    if G[x][y] == "#":
        return
    if cost[x][y] <= c:
        return
    cost[x][y] = c
    Q.append((x, y))


# 幅優先探索
while len(Q) >= 1:
    x, y = Q.popleft()
    c2 = cost[x][y] + 1
    # 四隅の検索
    push(x - 1, y, c2)
    push(x, y - 1, c2)
    push(x + 1, y, c2)
    push(x, y + 1, c2)

# print(cost)
print(cost[gx][gy])
