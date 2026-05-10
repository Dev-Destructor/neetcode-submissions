class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for idx, num in enumerate(nums):
            if num in dict:
                return True
            dict[num] = idx
        return False

        