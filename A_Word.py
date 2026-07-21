a=input() 

lower=0
upper=0

for ch in a:
    if ch.islower() > ch.isupper() :
        print(a.lower)
    elif ch.islower < ch.isupper():
        print(a.upper())
    else:
        print(a.lower()