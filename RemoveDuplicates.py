# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Given nums = [1,1,2],
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the returned length.

# Example 2:
# Given nums = [0,0,1,1,1,2,2,3,3,4],
# Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
# It doesn't matter what values are set beyond the returned length.

# Solution1:
# class solution:
#     def removeduplicates(self, nums:[int])->int:
#         i=0
#         while i<len(nums)-1:
#             if nums[i]==nums[i+1]:
#                 nums.remove(nums[i])
#             else:
#                 i+=1
#         return len(nums)

# Solution2:
class solution:
    def removeduplicates(self,nums:[int])->int:
        dif_num=1
        if nums==[]:
            return 0

        for i in range(len(nums)):
            if(i+1<len(nums)):
                if nums[i]<nums[i+1]:
                    nums[dif_num]=nums[i+1]
                    dif_num+=1            
        print(nums)
        return dif_num




print(solution.removeduplicates(solution,[1,1,2]))
print(solution.removeduplicates(solution,[0,0,1,1,1,2,2,3,3,4]))