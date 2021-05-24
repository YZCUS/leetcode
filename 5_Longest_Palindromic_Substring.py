# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
# Input: "cbbd"
# Output: "bb"


class solution: 
    def LongestPalindrome(self,s:str)-> str:








        # a="" # this solution works however the time complexity and space complexity are too high, we have to reduce time to pass the exam
        # for i in range(len(s)):
        #     for j in range(len(s)):
        #         if j>=i and s[i:j+1]==s[i:j+1][::-1] and j-i+1>len(a):
        #             a=s[i:j+1]
        # return a
print(solution.LongestPalindrome(solution,"babad"))
print(solution.LongestPalindrome(solution,"cbbd"))
print(solution.LongestPalindrome(solution,"zoozssawwqqqqq"))