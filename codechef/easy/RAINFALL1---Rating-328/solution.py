t=int(input())
for _ in range(t):
    a=int(input())
    if 3>a:
        print("LIGHT")
    elif a>=3 and 7>a:
        print("MODERATE")
    else:
        print("HEAVY")