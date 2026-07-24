class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums)-1
        # lst_m = nums[l + (r-l)//2]

        while l <= r:
            m = l + (r-l)//2


            if nums[m] < nums[m-1]:
                return nums[m]
            
            elif nums[m] < nums[0]:
                r = m-1

            else:
                l = m+1


            # lst_m = nums[m]
        
        return nums[0]