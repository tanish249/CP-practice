t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=abs(a-b)
    if c>=h:
        print("YES")
    else:
        print("NO")