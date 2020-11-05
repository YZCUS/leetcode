# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next=None

class solution:
    def addTwoNumbers(self,l1:ListNode,l2:ListNode):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=R=ListNode(0)
        flag=0 #用來標記是否進位
        
        while l1 and l2:
            if flag==1:
                add=l1.val+l2.val+1
                l1=l1.next
                l2=l2.next
            else:
                add=l1.val+l2.val
                l1=l1.next
                l2=l2.next
            if add>=10:
                flag=1
                add=add-10
                R=ListNode(add)
                R=R.next
            else:
                flag=0
                R=ListNode(add)
                R=R.next
        return head.next

print(solution.addTwoNumbers())