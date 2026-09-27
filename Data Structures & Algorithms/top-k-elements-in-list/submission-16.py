class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        #the 'in' might be a problem, replace with try, except if O > O(n)
        for num in nums:
            try:
                counter[num] += 1
            except: 
                counter[num] = 1
        
        for num, count in counter.items():
            freq[count].append(num)

        for i in range(len(freq) - 1, -1, -1):
            if freq[i]:
                for num in freq[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
                