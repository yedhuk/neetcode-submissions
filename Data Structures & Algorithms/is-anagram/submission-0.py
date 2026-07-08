class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq = {}
        t_freq = {}
        for i,c in enumerate(s):
            s_freq[c] = s_freq.get(c,0) + 1

        for i,c in enumerate(t):
            t_freq[c] = t_freq.get(c,0) + 1

        if s_freq == t_freq:
            return True

        return False
            