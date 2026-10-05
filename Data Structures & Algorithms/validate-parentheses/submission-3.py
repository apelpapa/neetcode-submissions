class Solution:
    def isValid(self, s: str) -> bool:
        isLoop = False
        pairs = ["{}", "()", "[]"]

        while s and not isLoop:
            isLoop = True
            for pair in pairs:
                if pair in s:
                    index = s.find(pair)
                    if index == 0:
                        s = s[2:]
                    else:
                        s = s[:index] + s[index+2:]
                    isLoop = False
        
        return True if len(s) == 0 else False