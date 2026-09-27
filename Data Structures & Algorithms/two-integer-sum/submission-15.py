class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            num_target = target - num
            if num_target in nums:
                num_target_index = nums.index(num_target)
                if num_target_index == i:
                    try:
                        num_target_index = nums.index(num_target, num_target_index + 1)
                    except: 
                        continue
                temp_arr = [i, num_target_index]
                return sorted(temp_arr)