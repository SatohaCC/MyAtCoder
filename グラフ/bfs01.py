import io
import sys

_INPUT = """\
5 2
4 1
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 幅優先探索　重みなし無向グラフ　　キュー
# 指定回数（今回は３回）で到達できる場所を求める
# ---------------------------------------------------------------------------------------------------------


from collections import deque

# 表のサイズ
H, W = map(int, input().split())

# スタート地点
y, x = map(int, input().split())

Q = deque()
Q.append((y, x))

dist = [[-1] * W for _ in range(H)]

# 距離（移動回数）の確認表
dist[y][x] = 0

mp = [["."] * W for _ in range(H)]
mp[y][x] = "*"


# 幅優先探索
while len(Q) >= 1:

    ny, nx = Q.popleft()
    if dist[ny][nx] == 3:
        continue

    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        # 未到達を到達にする
        if 0 <= dy + ny < H and 0 <= dx + nx < W:
            if dist[dy + ny][dx + nx] == -1:
                # 現在地+1の距離を設定
                dist[dy + ny][dx + nx] = dist[ny][nx] + 1
                mp[dy + ny][dx + nx] = "*"
                Q.append((dy + ny, dx + nx))


for i in range(H):
    print(*mp[i], sep="")
