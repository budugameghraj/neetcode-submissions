class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        maxlen=0
        for i in seen:
            length=0
            if i-1 in seen:
                continue
            if i-1 not in seen:
                start=i
            while start in seen:
                length+=1
                start+=1
            if length>maxlen:
                maxlen=length
        return maxlen