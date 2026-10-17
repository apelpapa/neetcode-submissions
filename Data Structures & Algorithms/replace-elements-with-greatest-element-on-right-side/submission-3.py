class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest_met = arr[-1]
        arr = arr [1:]

        arr = arr[::-1]
        for i, num in enumerate(arr):
            if num <= largest_met:
                arr[i] = largest_met
            else:
                largest_met = num

        arr = arr[::-1]
        arr.append(-1)       
        return arr
