class Solution:
    
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()

        new_s = ""

        for i in range(len(s)):
            if s[i].isalnum():
                new_s = new_s + s[i]

        rev = ""

        for i in range(-1, -len(new_s)-1, -1):
            rev = rev + new_s[i]

        if new_s == rev:
            return True
        else:
            return False