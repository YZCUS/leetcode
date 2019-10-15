# Given a string, find the length of the longest substring without repeating characters.

# Example 1:
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 

# Example 2:
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class solution:
    def longest_substring(self,s:str) ->int:
        a=""
        b=""
        for i in range(len(s)):
            for j in range(len(s)):
                if j>=i:
                    for k in range(j-i+1):
                        if s[i:j+1][k] not in b:
                            b+=s[i:j+1][k]    
                    if len(b)>len(a) and b in s:
                        a=b
        return a,len(a)

print(solution.longest_substring(solution,"abcabcbb"))
print(solution.longest_substring(solution,"bbbbbbb"))
print(solution.longest_substring(solution,"pwwkew"))