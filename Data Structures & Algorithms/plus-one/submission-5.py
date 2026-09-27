class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        digits = digits[::-1]
        for i, digit in enumerate(digits):
            if i == len(digits) - 1:
                break
            if digits[i] >= 10:
                digits[i] -= 10
                digits[i+1] += 1
        
        if digits[-1] >= 10:
            digits[-1] -= 10
            digits.append(1)

        return digits[::-1]
