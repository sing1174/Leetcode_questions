class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


        k = 0
        for i in range(len(nums)):
            if k<2 or nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k+=1
        return k
        