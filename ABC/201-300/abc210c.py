import io
import sys

_INPUT = """\
7 3
1 2 3 4 5 6 7

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 差分計算をする
#
# ---------------------------------------------------------------------------------------------------------


N, K = map(int, input().split())
C = list(map(int, input().split()))

dic = {}
# 初期化
for i in range(K):
    if C[i] not in dic:
        dic[C[i]] = 1
    else:
        dic[C[i]] += 1

kinds = len(dic.keys())

ans = kinds

for i in range(N - K):
    # print(i, C[i], C[i + K])
    # iを1つマイナスして
    dic[C[i]] -= 1
    # 完全に０なら種類を－１してから削する
    if dic[C[i]] == 0:
        kinds -= 1
        del dic[C[i]]

    # i+Kを入れる
    if C[i + K] not in dic:
        dic[C[i + K]] = 1
        kinds += 1
    else:
        dic[C[i + K]] += 1

    ans = max(ans, kinds)
print(ans)
