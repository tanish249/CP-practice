t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if a>b:
        print("SECOND")
    elif a<b:
        print('FIRST')
    elif a==b:
        print("ANY")