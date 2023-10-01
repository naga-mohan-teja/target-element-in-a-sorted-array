# nums=[4,5,6,7,0,1,2]
nums=[7,8,1,2,3,4,5,6]
# nums=[4,5,1,2,3]
lo=0
hi=len(nums)-1
while(lo<=hi):
    mid=(lo+hi)//2
    if nums[mid-1]>=nums[mid]:
        print(nums[mid])
        break
    if nums[mid]>nums[hi]:
        lo=mid+1
    else:
        hi=mid-1
