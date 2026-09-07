class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total=0
        count=0
        seen={0:1}
        for i in range(len(nums)):
            total+=nums[i]
            x=total-k
            if x in seen:
                count+=seen[x]
            if total not in seen:
                seen[total]=0
            seen[total]+=1
        return count
        