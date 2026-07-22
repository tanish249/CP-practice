t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=a+b+c+d
    if h>=1:
        print("OUT")
    else:
        print("IN")