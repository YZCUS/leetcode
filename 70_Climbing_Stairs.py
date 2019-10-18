# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Note: Given n will be a positive integer.

# Example 1:
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class solution:
    def climbstairs(self,n:int)->int:
        
        # s=0
        # for i in range(n//2+1):
        #     a=1
        #     b=1
        #     c=1
        #     for j in range(n-i):
        #         a*=(j+1)
        #     for j in range(i):
        #         b*=(j+1)
        #     for j in range(n-2*i):
        #         c*=(j+1)
        #     s+=(a/b/c)
        # return int(s)

        l,r=1,1
        for _ in range(n-1):
            l,r=r,l+r
        return r



print(solution.climbstairs(solution,1))
print(solution.climbstairs(solution,5))
print(solution.climbstairs(solution,6))