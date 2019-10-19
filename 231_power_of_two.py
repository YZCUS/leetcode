# Given an integer, write a function to determine if it is a power of two.

# Example 1:

# Input: 1
# Output: true 
# Explanation: 20 = 1
# Example 2:

# Input: 16
# Output: true
# Explanation: 24 = 16
# Example 3:

# Input: 218
# Output: false


class solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # for i in range(0,16):
        #     if n==(1<<i):
        #         return True
        # return False

        # if n==0:
        #     return False
        # elif n==1:
        #     return True
        # else:
        #     while n>1:
        #         if n%2==1:
        #             return False
        #         else:
        #             n /= 2
        #     return True


        if n<1: return False
        if n==1: return True
        while n>1:
            if n%2==1: return False
            n//=2
        return True
print(solution.isPowerOfTwo(solution,2))
