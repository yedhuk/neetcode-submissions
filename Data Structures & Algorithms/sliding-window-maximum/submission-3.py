class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # k = 3  # Window size
        result = []
        max_heap = []

        # 1. Process the first window [1, 2, 1]
        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))

        # The top of the heap is the max for the first subset
        result.append(-max_heap[0][0])

        # 2. Slide the window across the rest of the array
        for i in range(k, len(nums)):
            # Add the new element entering the window
            heapq.heappush(max_heap, (-nums[i], i))
            
            # Clean up: Remove the max element if it belongs to an old window
            while max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
                
            # The top of the heap is now the valid maximum for the current window
            result.append(-max_heap[0][0])
        
        return result