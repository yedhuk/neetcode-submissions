class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)

        l = 0
        r = n-1

        A = []

        for i,m in enumerate(nums):
            A.append([m,i])

        A.sort()

        while l<r:
            if (A[l][0] + A[r][0]) == target:
                return [min(A[l][1], A[r][1]),
                        max(A[l][1], A[r][1])]

            if (A[l][0] + A[r][0]) > target:
                r -= 1

            if (A[l][0] + A[r][0]) < target:
                l += 1

        return []
            