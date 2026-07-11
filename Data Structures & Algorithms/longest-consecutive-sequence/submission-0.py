class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            length = 0
            if (num-1) not in numSet:
                # i = 0
                for i in range(len(numSet)):
                    if (num + i) in numSet:
                        length +=1

                    else:
                        break
                
                longest = max(length,longest)

        return longest

            

