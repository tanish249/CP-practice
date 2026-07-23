t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h= a + b
    j= b + c
    k= a + c
    if(h==c):
        print("YES")
    elif(j==a):
        print("YES")
    elif(k==b):
        print("YES")
    else:
        print("NO")