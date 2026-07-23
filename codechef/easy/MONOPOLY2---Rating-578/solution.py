t=int(input())
for _ in range(t):
    nums=list(map(int,input().split()))
    nums.sort()
    h=nums[0]+nums[1]+nums[2]
    if nums[3]>h:
        print("YES")
    else:
        print("NO")