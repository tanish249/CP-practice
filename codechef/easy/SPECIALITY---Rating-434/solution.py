t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if a>b and a>c:
        print("Setter")
    elif b>a and b>c:
        print("Tester")
    elif c>a and c>b:
        print("Editorialist")