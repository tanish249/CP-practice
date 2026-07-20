t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=abs(a-b)
    g=h*2
    if a>=b:
        print(b)
    elif b>a:
        print(a+g)