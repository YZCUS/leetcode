"""
if there is list, we'd like to judge if a element is bigger than or equal to the previous one.
"""
#regular codes
nums=[1,2,3,3,5,6,6,7]
def checker(l):
    for x in range(len(l)):
        if x+1 < len(l):
            if l[x]>l[x+1]:
                return False
    return True
# print(checker(nums))

def checker2(l):
    return all(i<=j for (i, j) in zip(l, l[1:]))
print(checker2(nums))
print(list(zip(nums, nums[1:])))
print(list(zip(*zip(nums, nums[1:]))))
