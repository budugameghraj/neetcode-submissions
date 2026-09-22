class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        for x in nums:
            if x==2:
                count+=1
        r=0
        w=0
        while r<len(nums):
            if nums[r]==2:
                r+=1
            else:
                temp=nums[r]
                nums[r]=nums[w]
                nums[w]=temp
                r+=1
                w+=1
        i=0
        j=0
        while i<len(nums)-count:
            if nums[i]==1:
                i+=1
            else:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                i+=1
                j+=1
        return

        