class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d:
                return [d[complement], i]
            
            d[nums[i]] = i
        
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
            