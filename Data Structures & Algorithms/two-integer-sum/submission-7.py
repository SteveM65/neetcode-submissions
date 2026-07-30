class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, x in enumerate(nums):
            if target - nums[i] in hashmap:
                return [hashmap[target-x],i]
            hashmap[x] = i
        return  
        