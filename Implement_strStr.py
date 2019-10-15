# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

class solution:
    def Implement(self,haystack:str,needle:str)->int:
        if needle not in haystack:
            return -1
        elif needle=="":
            return 0
        else:
            return haystack.find(needle)

print(solution.Implement(solution,"hello","ll"))
print(solution.Implement(solution,"mississippi","issip"))