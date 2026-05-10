class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for idx, num in enumerate(nums):
            req = target - num
            if req in dict:
                return [dict[req], idx]
            dict[num] = idx