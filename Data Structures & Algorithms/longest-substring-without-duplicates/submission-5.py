class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch_set = set()
        left = 0
        max_count = 0
        count = 0

        for ch in s:
            while ch in ch_set:
                ch_set.remove(s[left])
                left += 1
                count -= 1
            
            count += 1
            ch_set.add(ch)

            if count > max_count:
                max_count = count
        return max_count