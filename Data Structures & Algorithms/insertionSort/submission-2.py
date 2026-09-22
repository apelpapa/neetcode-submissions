# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        outer = 1
        inner = 1
        pair_holder = []
        if pairs:
            pair_holder = [pairs.copy()]

        while outer < len(pairs):
            inner = outer
            while pairs[inner - 1].key > pairs[inner].key:
                temp_pair = pairs[inner]
                pairs[inner] = pairs[inner - 1]
                pairs[inner - 1] = temp_pair
                if inner > 1:
                    inner -= 1
                
            outer += 1
            pair_holder.append(pairs.copy())
        return pair_holder
            