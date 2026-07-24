t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=a*b
    g=c*24*60
    if g>=h:
        print("YES")
    else:
        print("NO")