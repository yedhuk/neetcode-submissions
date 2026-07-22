class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        
        for i,h in enumerate(heights):
            extend = 0

            # if stack and h > stack[-1][1]:
            

            if stack:
                if h <= stack[-1][1]:
                    while stack and h <= stack[-1][1]:
                        extend = i-stack[-1][0]
                        stack.pop()
                    stack.append((i-extend,h))
                    maxArea = max(maxArea,(i-stack[-1][0]+1)*(stack[-1][1]))

                else:
                    sl = -1 * len(stack)
                    j = -1
                    while j > (sl-1):
                        maxArea = max(maxArea,(i-stack[j][0]+1)*(stack[j][1]),h)
                        j-=1
                    stack.append((i-extend,h))

                # else:
                #     stack.append((i-extend,h))
            
            else:
                stack.append((i-extend,h))
                maxArea = max(maxArea,h)
            
            # area = (i-stack[-1][0]+1)*(stack[-1][1])
            # maxArea = max(maxArea,area)

        return maxArea

            


        