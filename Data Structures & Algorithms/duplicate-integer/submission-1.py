class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        h = {}

        for i, x in enumerate(nums):
            if x not in h:
                h[x] = i
            else:
                return True
        return False
        