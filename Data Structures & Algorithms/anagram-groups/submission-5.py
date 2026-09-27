class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        res = []

        for i, string in enumerate(strs):
            temp_string = list(string)
            temp_string.sort()
            temp_string = str(temp_string)
            if not res:
                res.append([string])
                str_dict[temp_string] = 0
                continue
            if temp_string in str_dict:
                res[str_dict[temp_string]].append(string)
            else:
                str_dict[temp_string] = len(res)
                res.append([string])

        return res