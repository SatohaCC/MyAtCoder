# 切り上げて数えるパターン

import io
import sys

_INPUT = """\
7

"""
sys.stdin = io.StringIO(_INPUT)


# ---------------------------------------------------------------------------------------------------------


N = int(input())

print((N + 2 - 1) // 2)
