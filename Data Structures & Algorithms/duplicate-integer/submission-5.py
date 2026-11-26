class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        h = {}

        #Convert list to dict:

        for i in nums:
            if i not in h:
                h[i] = 1
            else:
                return True
        return False