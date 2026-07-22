t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=7*a
    print(abs(h-b))