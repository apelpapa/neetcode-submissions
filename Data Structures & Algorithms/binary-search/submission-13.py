class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        if len(nums) < 1:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1

        def binary_search(nums, left, right, target):
            middle = ((right - left) // 2) + left
            if middle >= len(nums):
                return -1
            print(left, right, middle)
            if nums[middle] == target:
                return middle
            if right == left:
                return -1
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
            
            if right < left:
                return -1
            return binary_search(nums, left, right, target)

        return binary_search(nums, left, right, target)