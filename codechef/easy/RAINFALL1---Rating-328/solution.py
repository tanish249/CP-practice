t=int(input())
for _ in range(t):
    a=int(input())
    if 3>a:
        print("LIGHT")
    elif a>=3 and a<7:
        print("MODERATE")
    else:
        print("HEAVY")