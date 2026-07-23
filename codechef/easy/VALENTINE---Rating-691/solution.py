t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if a>b:
        print(int(a/b))
    else:
        print(0)