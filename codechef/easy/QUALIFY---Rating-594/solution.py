t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=b+c*2
    if h>=a:
        print("Qualify")
    else:
        print("NotQualify")