#lowest bound (>=)
arr=[1,2,3,3,5,8,8,10,10,11]
#ar=[0,1,2,3,4,5,6, 7, 8, 9]
target=3
lo=0
hi=len(arr)-1
while(lo<=hi):
    mid=(lo+hi)//2
    if arr[mid]==target:
        print(mid)
        break
    else:
        if arr[mid]<target:
            lo=mid+1
        else:
            hi=mid-1
else:
    print(lo)

#############################################################
#Higher bound(<=)
arr=[11,22,33,37,93,111,131,157]
#ar=[ 0, 1, 2, 3, 4,  5,  6,  7]
target=23
lo=0
hi=len(arr)-1
while(lo<=hi):
    mid=(lo+hi)//2
    if arr[mid]<=target:
        lo=mid+1
    else:
        hi=mid-1
else:
    print(lo)
