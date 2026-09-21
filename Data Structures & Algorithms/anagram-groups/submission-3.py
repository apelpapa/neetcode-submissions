class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pair_holder = []
        temp_dic = {}
        for index, strg in enumerate(strs):
            #print("\n", index, strg)
            temp_list = list(strg)
            temp_list.sort()
            temp_list = str(temp_list)
            if temp_list == "[]":
                #print(123)
                temp_list = "1"

            if temp_list in temp_dic:
                #print(temp_list)
                #print(temp_dic[temp_list])
                pair_holder[temp_dic[temp_list]].append(strg)
                #print(pair_holder)
            else:
                temp_dic[temp_list] = len(pair_holder)
                pair_holder.append([strg])
                #print(pair_holder)

        return pair_holder