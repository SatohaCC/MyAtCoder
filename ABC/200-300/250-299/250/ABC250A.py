import io
import sys

_INPUT = """\
4 1
4 1




"""
sys.stdin = io.StringIO(_INPUT)



# ---------------------------------------------------------------------------------------------------------



h,w= map(int, input().split())
r,c= map(int, input().split())

if h>=3 and w>=3:
    if (r == h and c==w) or (r==1 and c==1) or (r==h and c==1)or(r==1 and c==w):
        print(2)
    elif (r==h and 2<=c<w) or(r==1 and 2<=c<w) or(2<=r<h and c==w)or(2<=r<h and c==1):
        print(3)
    else:
        print(4)
elif h>=2 and w>=2:
    if (r == h and c==w) or (r==1 and c==1) or (r==h and c==1)or(r==1 and c==w):
        print(2)
    elif (r==h and 2<=c<w) or(r==1 and 2<=c<w) or(2<=r<h and c==w)or(2<=r<h and c==1):
        print(3)
elif h==1 and w==1:
    print(0)
elif h ==1 :
    if c==1 or c==w:
        print(1)
    elif 1<c<w:
        print(2)
elif w ==1 :
    if r==1 or r==h:
        print(1)
    elif 1<r<h:
        print(2)