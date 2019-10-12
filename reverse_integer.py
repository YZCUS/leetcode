# Given a 32-bit signed integer, reverse digits of an integer.
# Example 1:
# Input: 123
# Output: 321

# Example 2:
# Input: -123
# Output: -321

# Example 3:
# Input: 120
# Output: 21

class solution:
    def reverseint(self,x:int) -> int:
        if x<0:
            return (-1)*int(str(abs(x))[::-1])
        else:
            return int(str(x)[::-1])

print(solution.reverseint(solution,123))
print(solution.reverseint(solution,-123))
print(solution.reverseint(solution,120))
print(solution.reverseint(solution,-910))