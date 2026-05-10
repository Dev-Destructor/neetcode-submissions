class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for idx, num in enumerate(nums):
            req = target - num
            if req in map:
                return [map[req], idx]
            map[num] = idx
        return [-1, -1]