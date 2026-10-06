# problem : Sorting an Array
# Approach : Merge Sort Algorithm 
# Time complexity : O(nlogn)
# Space complexity : O(n)
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        low=0
        high=len(nums)-1
        
        def divideArray(nums, low, high):
            if(low>=high):
                return 
            mid=(low+high)//2
            divideArray(nums, low, mid)       
            divideArray(nums, mid+1,high)
            mergeArray(nums, low, mid, high)
        
        def mergeArray(nuns, low, mid, high):
            temp=[]
            left=low
            right=mid+1
            while (left<=mid and right<=high):
                if(nums[left]<nums[right]):
                    temp. append(nums[left])
                    left+=1
                else:
                    temp. append(nums[right])
                    right+=1
            while(left<=mid):
                temp. append(nums[left])
                left+=1
            
            while(right <=high):
                temp. append(nums[right])
                right+=1
            for i in range(low, high+1):
                nums[i]=temp[i-low]
                
        divideArray(nums, low, high)
        return nums    
            
                   
                 
        
        
        
