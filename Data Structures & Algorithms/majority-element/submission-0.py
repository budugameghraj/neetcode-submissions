class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        n=len(nums)
        for i in nums:
            if i not in dict:
                dict[i]=0
            dict[i]+=1
        for key,value in dict.items():
            if dict[key]>n/2:
                return key


        