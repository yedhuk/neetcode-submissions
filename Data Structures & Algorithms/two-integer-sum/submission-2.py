class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        M = {}

        for i,n in enumerate(nums):
            M[n] = i

        for i,n in enumerate(nums):
            diff = target - n
            if diff in M and M[diff] !=i:
                return [i,M[diff]]

        return []
        