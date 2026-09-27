class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        #print(nums)
        count_arr = []
        counter = 0
        prev = None
        res = []

        if k == len(nums):
            return nums

        for i, num in enumerate(nums):
            if prev == None:
                prev = num
                counter += 1
            elif prev == num:
                counter += 1
            if prev != num:
                count_arr.append([counter, prev])
                counter = 1
                prev = num
            if i == len(nums) - 1:
                count_arr.append([counter, num])
        
        #print(count_arr)
        count_arr.sort()
        count_arr = count_arr[::-1]
        count_arr = count_arr[0: k]

        for count, num in count_arr:
            res.append(num)

        return res