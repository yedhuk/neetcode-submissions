class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numMap = {}
        for i,n in enumerate(nums):
            numMap[n] = i

        for i,n in enumerate(nums):
            if (target-n) in numMap:
                if i != numMap[(target-n)]:
                    return [i,numMap[(target-n)]]

        return None
        