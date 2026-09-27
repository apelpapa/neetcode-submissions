class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        arr = [False] * (len(s) + 1)
        arr[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i: i + len(word)] == word:
                    arr[i] = arr[i + len(word)]
                if arr[i]:
                    break
        print(arr)
        return arr[0]