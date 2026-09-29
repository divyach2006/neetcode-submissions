import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If concatenating the strings in both orders doesn't match,
        # it is mathematically impossible for them to share a divisor string.
        if str1 + str2 != str2 + str1:
            return ""
        
        # The length of the longest common divisor string will be 
        # the Greatest Common Divisor of the lengths of both strings.
        gcd_length = math.gcd(len(str1), len(str2))
        
        # Slice either string up to the calculated GCD length
        return str1[:gcd_length]
