t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if a>b:
        print("SECOND")
    elif b>a:
        print("FIRST")
    else:
        print("ANY")