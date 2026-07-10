class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encodedStr = ""
        for st in strs:
            # if st == "":
            #     continue
            encodedStr = encodedStr + str(len(st))+"#"+st
        print(encodedStr)
        return encodedStr

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res


        
