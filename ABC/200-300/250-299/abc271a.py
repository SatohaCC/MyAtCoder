import io
import sys

_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 10進数→16進数　アルファベットは大文字
# 02X を02xにするとアルファベットを小文字にできる
# ---------------------------------------------------------------------------------------------------------

n = int(input())
print(format(n, "02X"))
