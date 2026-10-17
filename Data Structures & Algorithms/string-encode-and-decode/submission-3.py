from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        # Map each string to its length + a '#' delimiter + the string itself
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        res = []
        i = 0
        
        while i < len(s):
            # Find the position of the delimiter '#' starting from index i
            j = s.find('#', i)
            
            # Extract and parse the length prefix
            length = int(s[i:j])
            
            # Step over the '#' character
            i = j + 1
            
            # Slice the string of known length and append to results
            res.append(s[i : i + length])
            
            # Advance the pointer past the sliced string
            i += length
            
        return res
