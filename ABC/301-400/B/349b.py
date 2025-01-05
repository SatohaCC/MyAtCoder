import io
import sys

_INPUT = """\
ab

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------


from collections import Counter

S = input().strip()

# 文字の出現回数を計算
counter = Counter(S)

# 0回または2回だけ出現するかどうかをチェック
is_zero_or_two = all(value == 0 or value == 2 for value in counter.values())

print("Yes" if is_zero_or_two else "No")
