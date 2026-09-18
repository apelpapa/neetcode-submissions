class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        addOne = True
        while i >= 0:
            if addOne:
                digits[i] += 1
                addOne = False
            
            if digits[i] > 9:
                if i-1 < 0:
                    digits[i] -= 10
                    digits.insert(0,1)
                else:
                    digits[i] -= 10
                    digits[i-1] += 1
            i -= 1
        return digits