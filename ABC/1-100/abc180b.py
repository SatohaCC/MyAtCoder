import io
import sys

_INPUT = """\
10
3 -1 -4 1 -5 9 2 -6 5 -3

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------

n = int(input())
a = list(map(int, input().split()))

# マンハッタン距離（Taxicab distance）
def Taxicab_distance(a):
    sum = 0
    for i in a:
        sum += abs(i)
    return int(sum)


print(Taxicab_distance(a))


# ユークリッド距離（Euclidean distance、Euclidean metric）
def Euclidean_distance(a):
    sum = 0
    for i in a:
        sum += abs(i) * abs(i)
    return sum**0.5


print(Euclidean_distance(a))

# チェビシェフ距離（英: Chebyshev distance）
def Chebyshev_distance(a):
    ans = 0
    for i in a:
        ans = max(ans, abs(i))
    return ans


print(Chebyshev_distance(a))
