class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_nums, max_nums = min(nums), max(nums)
        bucket = [0] * (max_nums - min_nums + 1)
        res = []

        for num in nums:
            bucket[num - min_nums] += 1

        for i in range(k):
            b_max = max(bucket)
            b_max_i = bucket.index(b_max)
            res.append(b_max_i + min_nums)
            bucket[b_max_i] = 0
        
        return res

