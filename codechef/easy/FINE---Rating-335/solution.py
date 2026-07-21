t=int(input())
for _ in range(t):
    a=int(input())
    if a<=70:
        print(0)
    elif a>70 and a<=100:
        print(500)
    elif a>100:
        print(2000)