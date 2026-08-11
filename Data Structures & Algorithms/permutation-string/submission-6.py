class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Maintain 2 windows and keep track of character frequency
        # Keep the window size constant

        if len(s1) > len(s2):
            return False

        s1Count =  [0]*26
        s2Count = [0]*26
        for c in s1:
            s1Count[ord(c)-ord('a')] += 1

        print(s1Count)

        l = 0
        

        for r in range(len(s2)):

            if r-l+1 < len(s1):
                s2Count[ord(s2[r])-ord('a')] += 1

            if r-l+1 == len(s1):
                s2Count[ord(s2[r])-ord('a')] += 1
                matchCount = 0
                print(f"l->{l}:r->{r}:{s2Count}")
                for i in range(26):
                    if (s1Count[i] - s2Count[i]) != 0 :
                        break
                    else:
                        matchCount += 1
                if matchCount == 26:
                    print(f"l->{l} : r->{r}")
                    return True

                if (r+1) < len(s2):
                    s2Count[ord(s2[l])-ord('a')] -= 1
                    # s2Count[ord(s2[r+1])-ord('a')] += 1
                    l+=1
        
        return False
                        
            