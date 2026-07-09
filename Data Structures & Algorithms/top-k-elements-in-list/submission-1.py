class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        freq_bucket = [[] for i in range(len(nums)+1)]
        k_list = []
        for item in nums:
            nums_dict[item] = nums_dict.get(item,0) + 1

        for item,count in nums_dict.items():
            freq_bucket[count].append(item)

        for i in range(len(freq_bucket)-1,-1,-1):
            if len(k_list) < k:
                k_list.extend(freq_bucket[i])

        return k_list[:k+1]

