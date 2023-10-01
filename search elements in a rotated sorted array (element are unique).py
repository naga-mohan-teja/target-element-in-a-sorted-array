
# search elements in a rotated sorted array 
#  when array element are unique
arr=[7,8,1,2,3,4,5,6]
#ar=[0,1,2,3,4,5,6,7]
target=6
lo=0
hi=len(arr)-1
while(lo<=hi):
    mid=(lo+hi)//2
    if arr[mid] == target:
        print(mid)
        break
    elif arr[lo]<=arr[mid]:
        if arr[lo]<=target and target < arr[mid]:
            hi=mid-1
        else:
            lo=mid+1
    else:
        if arr[mid]<target and target <= arr[hi]:
            lo=mid+1
        else:
            hi=mid-1
