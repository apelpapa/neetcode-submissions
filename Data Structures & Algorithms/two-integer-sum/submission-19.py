class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_targets = {}

        for i, num in enumerate(nums):
            new_target = target - num
            if new_target in hash_targets:
                return [hash_targets[new_target], i]
            hash_targets[num] = i