# Problem : Rotating Array Right by k steps
# Approach : Reversal Algorithm + Two pointers
# Time complexity : O(n)
# Space complexity : O(1)
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        
        """
        Do not return anything, modify nums in-place 
        instead.
        """
        n=len(nums)
        k=k%n
        
        
        i=0
        j=n-1
        while i<j:
            nums[i], nums[j]=nums[j], nums[i]
            i+=1
            j-=1
            
            
        i=0
        j=k-1
        
        while i<j:
            nums[i], nums[j]=nums[j], nums[i]
            i+=1
            j-=1
        
        i=k
        j=n-1
        
        while i<j:
            nums[i], nums[j]=nums[j], nums[i]
            i+=1
            j-=1
            
            
     
        
        
