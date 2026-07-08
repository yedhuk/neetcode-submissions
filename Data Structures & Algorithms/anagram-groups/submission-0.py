class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        OHE_dict = {}
        for word in strs:
            OHE = [0]*26
            for i,c in enumerate(word):
                OHE[ord(c) - ord('a')] +=1
            OHE_tuple = tuple(OHE)
            if OHE_tuple in OHE_dict:
                OHE_dict[OHE_tuple].append(word)
            else:
                OHE_dict[OHE_tuple] = []
                OHE_dict[OHE_tuple].append(word)

        final = []
        for ohe,words in OHE_dict.items():
            final.append(words)

        return final



        
        