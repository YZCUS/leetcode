# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class solution:
    def twosum(self,nums,target):
        """
        :type nums:list[int]
        :type target:int
        :rtype: list[int]
        """
        dict={}
        for i in range(len(nums)):
            if target-nums[i] not in dict:
                dict[nums[i]]=i
            else:
                return [dict[target-nums[i]],i]

print(solution.twosum(solution,[2,7,11,15],17))