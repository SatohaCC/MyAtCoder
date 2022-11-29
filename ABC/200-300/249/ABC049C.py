import io
import sys
_INPUT = """\
erasedream
"""
sys.stdin = io.StringIO(_INPUT)




import re


S = input()



'''
メタ文字：
^ = 文字列の先頭、
| = OR
+ = 直前のパターンを1回以上繰り返し、
$ = 文字列の末尾
'''



if re.match("^(dream|dreamer|erase|eraser)+$", S):
    print('YES')
else:
    print('NO')




#別海
a = ["eraser", "erase", "dreamer", "dream"]

S = input()
for i in range(4):
    S = S.replace(a[i],"")
    print(S)