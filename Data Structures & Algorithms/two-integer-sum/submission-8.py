class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            spread = target - num
            if spread in nums:
                spread_index = nums.index(spread)
                if index != spread_index:
                    if spread_index < index:
                        return [spread_index, index]
                    return [index, spread_index]
            