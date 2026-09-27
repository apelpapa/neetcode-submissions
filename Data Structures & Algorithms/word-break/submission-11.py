class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict:
            return True
        sl = list(s)
        counter = 0
        
        while counter < len(sl) and sl:
            temp_s = sl[counter:]
            temp_s = "".join(temp_s)
            if temp_s in wordDict:
                sl = sl [:counter]
                counter = 0
                continue
            counter += 1


        if len(sl) == 0:
            return True
        sl = list(s)
        counter = 1

        while counter <= len(sl) and sl:
            temp_s = sl[:counter]
            temp_s = "".join(temp_s)
            if temp_s in wordDict:
                sl = sl [counter:]
                counter = 1
                continue

            counter += 1
        
        if len(sl) == 0:
            return True
        return False