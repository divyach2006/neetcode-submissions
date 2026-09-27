class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        
        def backtrack(current_str, open_count, close_count):
            # Base case: if the string reaches the maximum valid length
            if len(current_str) == 2 * n:
                result.append(current_str)
                return
            
            # Rule 1: You can always add an open parenthesis if you haven't used all n
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, close_count)
                
            # Rule 2: You can only add a close parenthesis if it matches an open one
            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count + 1)
                
        # Start the recursion with an empty string and 0 counts
        backtrack("", 0, 0)
        return result
