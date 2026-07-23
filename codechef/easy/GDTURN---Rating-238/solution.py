t = int(input())
for i in range(0,t):
    x,y = map(int,input().split())
    h=x+y
    if h>6:
        print("YES")
    else:
        print("NO")