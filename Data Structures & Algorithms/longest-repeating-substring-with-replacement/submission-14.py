class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = defaultdict(int)
        l = 0
        # most_freq = 0
        res = 0
        r = 0
        prev_r = -1
        while r < len(s):
            
            if prev_r != r:
                freq[s[r]] += 1
            # most_freq = max(most_freq,freq[s[r]])
            most_freq = 0
            
            for i in range(0,26):
                most_freq = max(most_freq,freq[chr(ord('A') + i)])
            # print(freq)
            
            # print(f"most_freq :{most_freq}")


            window_len = r-l+1

            if (window_len - most_freq) <= k:
                res = max(res,r-l+1)
                # print(f"res :{res}")
                prev_r = r
                r+=1
                continue

            else:
                
                freq[s[l]]-=1
                l+=1
                prev_r = r

        return res






                    

