# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
# The median is 2.0

# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# The median is (2 + 3)/2 = 2.5

class solution:
    def findMedianSortedArrays(self, nums1:[int], nums2:[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        return nums1[len(nums1)//2] if len(nums1)%2==1 else (nums1[int(len(nums1)/2)-1]+nums1[int(len(nums1)/2)])/2


print(solution.findMedianSortedArrays(solution,[1,3],[2]))
print(solution.findMedianSortedArrays(solution,[1,2],[3,4]))
