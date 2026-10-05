class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            new_target = target - num
            if new_target in nums:
                index = nums.index(new_target)
                if index == i:
                    continue
                return [i, index] if index > i else [index, i]