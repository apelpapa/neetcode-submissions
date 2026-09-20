class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp_set = set()
        for num in nums:
            if num in temp_set:
                return True
            temp_set.add(num)
        return False