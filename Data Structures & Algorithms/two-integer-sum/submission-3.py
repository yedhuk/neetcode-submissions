class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        M = {}

        for i,n in enumerate(nums):
            diff = target - n

            if diff in M:
                return [M[diff],i]

            M[n] = i
        