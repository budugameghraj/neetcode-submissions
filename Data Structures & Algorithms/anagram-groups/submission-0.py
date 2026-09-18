class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        soln={}
        for i in range(len(strs)):
            dict={}
            for j in range(len(strs[i])):
                if strs[i][j] not in dict:
                    dict[strs[i][j]]=0
                dict[strs[i][j]]+=1
            key=tuple(sorted(dict.items()))
            if key not in soln:
                soln[key]=[]
            soln[key].append(strs[i])
        return list(soln.values())

        