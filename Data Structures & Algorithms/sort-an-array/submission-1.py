class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        left=nums[:mid]
        right=nums[mid:]
        left=self.sortArray(left)
        right=self.sortArray(right)
        i=0
        j=0
        result=[]
        while i<len(left) and j<len(right):
            if left[i]>right[j]:
                result.append(right[j])
                j+=1
            elif right[j]>left[i]:
                result.append(left[i])
                i+=1
            else:
                result.append(left[i])
                result.append(right[j])
                i+=1
                j+=1
        while i<len(left):
            result.append(left[i])
            i+=1
        while j<len(right):
            result.append(right[j])
            j+=1
        return result