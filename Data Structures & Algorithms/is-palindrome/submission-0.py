class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = re.sub(r'[^A-Za-z0-9]', '', s.lower().strip())
        print(cleaned_text)
        j = len(cleaned_text)-1
        for i in range(len(cleaned_text)):
            

            if cleaned_text[i] != cleaned_text[j]:
                return False
            j = j-1
        return True


                
        