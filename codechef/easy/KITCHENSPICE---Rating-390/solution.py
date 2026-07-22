t=int(input())
for _ in range(t):
    a=int(input())
    if 4>a:
        print("MILD")
    elif a>=4 and 7>a:
        print("MEDIUM")
    elif a>=7:
        print("HOT")