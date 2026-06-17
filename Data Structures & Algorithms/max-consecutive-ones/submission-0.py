class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k = 0
        c = 0
        best = 0
        for i in range(len(nums)):
            if nums[i] != 1:
                c = 0
            else:
                c+=1
                if c > best:
                    best = c
        return best

            
