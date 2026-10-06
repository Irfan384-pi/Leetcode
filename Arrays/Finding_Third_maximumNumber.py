# problem : Finding third maximum in an array
# approach : One pass three maximum number
# Time complexity : O(n)
# Space complexity : O(1)
class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        n=len(nums)
        largest=nums[0]
        second_largest=None
        third_largest=None 
        
        for i in range(n):
            if(nums[i]>largest ):
                third_largest=second_largest
                second_largest=largest
                largest=nums[i]
            elif nums[i]<largest:
                if second_largest is None or nums[i]>second_largest:
                    third_largest=second_largest
                    second_largest=nums[i]
                elif nums[i]<second_largest:
                    if third_largest is None or nums[i]>third_largest:
                        third_largest=nums[i]
           
        if third_largest is None:
            return largest
        return third_largest
                
