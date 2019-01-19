a,b,c=map(int ,input().split())
# print(a,b,c)
# print(type(a))
if 0<a<180  and 0<b<180 and 0<c<180 and a+b+c==180:
    if a==b==c:
        print('等边三角形')
    elif a<90 and b<90 and c<90:
        print('锐角三角形')
    elif a>90 or b>90 or c>90:
        print('钝角三角形')
    elif a==90 or b==90 or c==90:
        print('直角三角形')
else:
    print('无法构成三角形')
