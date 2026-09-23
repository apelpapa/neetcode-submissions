class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits:
            digits_reversed = digits[::-1]
            digits_reversed[0] += 1
        

        for i, digit in enumerate(digits_reversed):
            print(digit)
            if digit >= 10 and not i + 1 == len(digits_reversed):
                digits_reversed[i] -= 10
                digits_reversed[i + 1] += 1
            elif digit >= 10:
                digits_reversed[i] -= 10
                digits_reversed.append(1)
            print(digit, "\n")
        return digits_reversed[::-1]