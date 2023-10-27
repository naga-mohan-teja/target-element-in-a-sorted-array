import sys
class Solution:
    def findClosest(self, arr, n, target): 
      
        # Complete the function
        start = 0
        end = n-1
        close=sys.maxsize
        result=-1
        while(start<=end):
            mid= (start + end)//2
            diff = abs(arr[mid] - target)
            if(diff < close or (diff == close and arr[mid]>result)):
                close = diff
                result = arr[mid]
            
            if(arr[mid] > target):
                end = mid-1
            else:
                start=mid+1
        return result
