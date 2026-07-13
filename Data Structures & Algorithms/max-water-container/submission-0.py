class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        # l = n // 2
        # r = l + 1

        l = 0
        r = n-1
        max_capacity = 0

        while l<r :

            capacity = min(heights[l],heights[r])*(r-l)
            max_capacity = max(max_capacity,capacity)

            if heights[l] < heights[r]:
                l += 1

            elif heights[r] < heights[l]:
                r -= 1
            
            elif heights[r] == heights[l]:
                l += 1
                r -= 1

            
        return max_capacity



        