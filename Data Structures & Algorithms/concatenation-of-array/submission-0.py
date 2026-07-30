class Solution:
    def getConcatenation(self,nums):
        n=len(nums)
        ans=[0]*2*n
        for i, num in enumerate(nums):
            ans[i]=ans[i+n]=num
        return ans