# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Example 1:
# Input: 16
# Output: true
# Example 2:
# Input: 5
# Output: false



class solution:
    def poweroffour(self,num:int)->int:
        # if 2**32>num>0:
        #     i=0
        #     while 4**i<=num:
        #         if 4**i!=num:
        #             i+=1
        #         else:
        #             return 4**i==num
        #     return 4**i==num



        for i in range(0,16):
            if num == (1<<(2*i)):
                return True
        return False


print(solution.poweroffour(solution,8))
print(solution.poweroffour(solution,16))
print(solution.poweroffour(solution,36))
print(solution.poweroffour(solution,256))