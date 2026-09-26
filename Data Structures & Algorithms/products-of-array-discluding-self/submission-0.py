class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        left=[]
        left_product=1
        right=[]
        right_product=1
        for i in range(len(nums)):
            left.append(left_product)
            left_product*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            right.append(right_product)
            right_product*=nums[i]
        right=right[::-1]
        for i in range(len(nums)):
            res.append(left[i]*right[i])
        return res
        