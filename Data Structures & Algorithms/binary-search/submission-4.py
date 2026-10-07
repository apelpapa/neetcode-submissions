class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        higher = len(nums)

        if nums[0] == target:
            return 0

        return self.binarySearch(nums, target, lower, higher)
    

    def binarySearch(self, nums, target, lower, higher):
        mid = ((higher - lower) // 2) + lower

        
        print(higher, mid, lower)
        if higher - mid == 1 and mid == lower:
            return -1
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lower = mid
            return self.binarySearch(nums, target, lower, higher)
        if nums[mid] > target:
            higher = mid
            return self.binarySearch(nums, target, lower, higher)