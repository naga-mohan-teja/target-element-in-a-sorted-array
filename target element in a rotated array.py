arr=list(map(int,input().split(",")))
target=int(input())
lo=0
hi=len(arr)-1
while(lo<=hi):   
    mid=(lo+hi)//2
    if arr[mid]==target:
        print(mid)
        break
    if arr[lo]<=arr[mid]:
        if arr[lo]<=target<arr[mid]:
            hi=mid-1
        else:
            lo=mid+1
    else:
        if arr[mid]<target<=arr[hi]:
            lo=mid+1
        else:
            hi=mid-1
else:
    print(-1)
