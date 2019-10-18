# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:
# Input: "()"
# Output: true
# Example 2:
# Input: "()[]{}"
# Output: true
# Example 3:
# Input: "(]"
# Output: false
# Example 4:
# Input: "([)]"
# Output: false
# Example 5:
# Input: "{[]}"
# Output: true

class solution:
    def valid_parentheses_1(self,s:str)->bool:
        dict={"(":")","[":"]","{":"}"}
        stack=[]
        for i in s:
            if i in dict:
                stack.append(i)
            elif not stack or i!=dict[stack.pop()]:
                return False
        return not stack

print(solution.valid_parentheses_1(solution,"()"))
print(solution.valid_parentheses_1(solution,"()[]{}"))
print(solution.valid_parentheses_1(solution,"(]"))
print(solution.valid_parentheses_1(solution,"([)]"))
print(solution.valid_parentheses_1(solution,"{[]}"))