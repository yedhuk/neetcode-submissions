class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = {} # More of a hash map approach same can done by a hash table approach as well using set
        for item in nums:
            if item in nums_set:
                return True
            else:
                nums_set[item] = 1
        
        return False