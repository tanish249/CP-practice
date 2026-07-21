t=int(input())
for _ in range(t):
    a=int(input())
    if(a<=3):
        print("BRONZE")
    elif(a>3 and a<=6):
        print("SILVER")
    elif(a>6):
        print("GOLD")