from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map character count tuple to list of anagrams
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Create a frequency array for 26 lowercase English letters
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
                
            # Convert list to an immutable tuple to use it as a dictionary key
            anagram_map[tuple(count)].append(s)
            
        # Return all grouped anagram lists
        return list(anagram_map.values())

