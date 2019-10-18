# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.
# Example:
# Input: "Hello World"
# Output: 5


class solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        # s=s.rstrip()
        # return s[::-1].find(" ") if " " in s else len(s)        
        
        l=s.split()
        return 0 if not l else len(l[-1])


print(solution.lengthOfLastWord(solution,"a    bb  "))