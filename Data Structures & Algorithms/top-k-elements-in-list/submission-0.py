class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        output=[]
        freq=[[]for i in range(len(nums)+1)]
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]]=0
            dict[nums[i]]+=1
        for key,value in dict.items():
            freq[value].append(key)
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                output.append(n)
                if len(output)==k:
                    return output
        