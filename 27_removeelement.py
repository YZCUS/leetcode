class solution:
    def removeElement(self, nums: [int], val: int) -> int:
        # for i in range(len(nums)):
        i=0
        while i<len(nums):
            if nums[i]==val:
                nums.remove(val)
                i-=1
            i+=1
        return nums,len(nums)

print(solution.removeElement(solution,[3,2,2,3],3))
print(solution.removeElement(solution,[0,1,2,2,3,0,4,2],2))