# B12 - Equation

import io
import sys


_INPUT = """\
87

"""
sys.stdin = io.StringIO(_INPUT)


def f(x):
    return x * x * x + x


N = int(input())

# 二分探索
Left = 0.0
Right = 100.0 # max が100000なので100の３乗で超えるのでこれで十分

# ループが２０回なのは精度を計算してもとめる２の２の２０乗でOKなため
for _ in range(20):
    Mid = (Left + Right) / 2
    val = f(Mid)

    # 探索範囲を絞る
    if val > N:
        Right = Mid  # 左半分に絞られる
    else:
        Left = Mid  # 右半分に絞られる

# 出力
print(Mid)
