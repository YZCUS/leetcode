# Given an integer, write a function to determine if it is a power of three.

# Example 1:
# Input: 27
# Output: true
# Example 2:
# Input: 0
# Output: false
# Example 3:
# Input: 9
# Output: true
# Example 4:
# Input: 45
# Output: false
# Follow up:
# Could you do it without using any loop / recursion?

class solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:return False
        if n==1:return True
        while n>1:
            if n%3!=0:return False
            n//=3
        return True


print(solution.isPowerOfThree(solution,27))
print(solution.isPowerOfThree(solution,9))
print(solution.isPowerOfThree(solution,0))
print(solution.isPowerOfThree(solution,45))
