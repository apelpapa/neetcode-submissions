class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[-1] = -1
                break
            for j in range(len(arr)):
                if i > j:
                    continue
                if i == j:
                    arr[i] = arr[j + 1]
                if arr[j] > arr[i]:
                    arr[i] = arr[j]

        return arr