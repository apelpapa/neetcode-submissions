class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_list = []
        list_dict = {}
        res = []

        for string in strs:
            new_string = list(string)
            new_string.sort()
            list_list.append(new_string)

        for i, string in enumerate(list_list):
            temp_string = str(string)
            if not temp_string in list_dict:
                list_dict[temp_string] = [i]
            else:
                list_dict[temp_string].append(i)

        for item in list_dict:
            res.append([])
            insert_index = len(res) - 1

            for i in list_dict[item]:
                res[insert_index].append(strs[i])

        return res