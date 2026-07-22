t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if b>a:
        print("PROFIT")
    elif a>b:
        print("LOSS")
    else:
        print("NEUTRAL")