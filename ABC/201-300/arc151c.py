import io
import sys

_INPUT = """\
5
00100
10011


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------

N = int(input())
S, T = input(), input()

count_s = S.count("1")
count_t = T.count("1")


if (count_s - count_t) % 2:
    # 異なる桁が奇数の場合は不可能
    ans = -1
    print(ans)
    exit()
elif count_s == count_t:
    # 全桁同じなら０埋めでOK
    ans = "0" * N
elif count_s > count_t:
    ans = ["0"] * N
    cnt = (count_s - count_t) // 2
    # Sのほうに１が多い場合
    for i in range(N - 1, -1, -1):
        if S[i] == "1" and T[i] == "0":
            ans[i] = "1"
            cnt -= 1
        if cnt == 0:
            break
else:
    ans = ["0"] * N
    cnt = (count_t - count_s) // 2
    for i in range(N - 1, -1, -1):
        if S[i] == "0" and T[i] == "1":
            ans[i] = "1"
            cnt -= 1
        if cnt == 0:
            break


print(*ans, sep="")
