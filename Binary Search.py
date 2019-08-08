a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
left=len(a)//2-1
right=len(a)

while left<right:
    if a[left]!=14:
        left+=(right-left)//2   #9//2=4
    else:
        break
print(a[left])
