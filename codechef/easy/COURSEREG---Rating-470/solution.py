t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=a+c 
    if b>=h:
        print("YES")
    else:
        print("NO")