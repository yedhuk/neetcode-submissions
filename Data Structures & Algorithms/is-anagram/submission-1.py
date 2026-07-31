class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sencode = [0]*26
        tencode = [0]*26

        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                sencode[ord(s[i])-ord('a')]+=1
                tencode[ord(t[i])-ord('a')]+=1

            if sencode == tencode:
                return True

            return False
                
