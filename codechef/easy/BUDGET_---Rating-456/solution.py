t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=b*30
    if a>=h:
        print("YES")
    else:
        print("NO")