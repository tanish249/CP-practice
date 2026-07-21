t=int(input())
a,b,c=map(int,input().split())
x,y,z=map(int,input().split())
p,q,r=map(int,input().split())
h=a+x+p
g=b+y+q
l=c+z+r
if(h==0 and g==0 and l==0):
    print("YES")
else:
    print("NO")

