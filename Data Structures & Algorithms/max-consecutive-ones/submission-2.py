class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter1 = 0
        counter2 = 0
        for index, num in enumerate(nums):
            print(counter1, counter2)
            if num == 1:
                counter2 += 1
            elif counter2 > counter1:
                counter1 = counter2
                counter2 = 0
            else: 
                counter2 = 0
            if index == len(nums)-1 and counter2 > counter1:
                counter1 = counter2
        return counter1
