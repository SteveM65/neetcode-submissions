class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        
        for i in range(len(nums)):
            #Calculate Difference
            diff = target - nums[i]
            #Check if Diff in Dict 
            if diff in dict1:
                return [dict1[diff], i]
            #Remember to add back to dictionary after check 
            dict1[nums[i]] = i
            
            