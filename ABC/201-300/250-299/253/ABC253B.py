import io
import sys

_INPUT = """\


"""
sys.stdin = io.StringIO(_INPUT)



# ---------------------------------------------------------------------------------------------------------


h,w= map(int, input().split())
maru_list =[]
for i in range(h):
    a = input()
    for j in range(w):
        if a[j] == "o":
            maru_list.append([i,j])

print(abs(maru_list[0][0]-maru_list[1][0])+abs(maru_list[0][1]-maru_list[1][1]))