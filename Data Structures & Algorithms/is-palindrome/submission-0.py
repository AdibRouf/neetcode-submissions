class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        
        s_text = ""
        for char in s:
            if char.isalnum():
                s_text += char
        s_text = s_text.lower()
        print (s_text)
        for i in range(len(s_text)):
            if s_text[p1] != s_text[-1 - i]:
                return False
            p1+=1
        return True 