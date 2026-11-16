class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            missing = target - num
            if missing not in seen:
                seen[num] = index
            else:
                return [seen[missing], index]
            
                