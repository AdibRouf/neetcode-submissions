class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashy = {}

        for i, n in enumerate(nums):
            if n in hashy:
                return True
            hashy[n] = i
        return False