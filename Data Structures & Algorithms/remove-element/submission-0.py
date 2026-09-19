class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r=0
        w=0
        while r<len(nums):
            if nums[r]==val:
                r+=1
            else:
                nums[w]=nums[r]
                r+=1
                w+=1
        return w
        