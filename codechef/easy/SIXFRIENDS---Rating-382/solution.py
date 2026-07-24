t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=a*3
    g=b*2
    if h>g:
        print(g)
    else:
        print(h)