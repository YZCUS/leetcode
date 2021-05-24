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
    def __init__(self, val, next= None): #define the structure of ListNode
        self.val = val
        self.next=next
def make_ListNode(elements): # create a ListNode from a list of elements
    head=ListNode(elements[0]) # initial element is defined as head
    for element in elements[1:]: # use the loop to create nodes and link them together
        currentNode=head
        while currentNode.next: # while the current node is not the tail, the currentnode keep traveresing toward the end.
            currentNode=currentNode.next
        currentNode.next=ListNode(element) # At the tail we assign a new ListNode linked to the end
    return head # reture the finished ListNode
def print_ListNode(head): # since we cannot directly print a ListNode, we have to create a function to print every nodes in the ListNode.
    print("[", end=" ")
    currentNode=head
    while currentNode is not None: # traverse to the last node and the currentNode will be None
        if currentNode.next is not None:
            print(currentNode.val, end=", ")
        else:
            print(currentNode.val, end=" ") # when print the last node, we don't want to end in "," 
        currentNode=currentNode.next
    print("]")
l1_1=make_ListNode([2,4,3])
l1_2=make_ListNode([5,6,4])
l2_1=make_ListNode([0])
l2_2=make_ListNode([0])
l3_1=make_ListNode([9,9,9,9,9,9,9])
l3_2=make_ListNode([9,9,9,9])
class solution():
    def addTwoNumbers(self,l1,l2): # define the solution to add two ListNode into one 
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=R=ListNode(0)
        flag=0 #用來標記是否進位 #initial flag is 0 
        
        while l1 and l2:
            if l1.next is None and l2.next is not None: # correct the different lengths of two ListNodes
                l1.next=ListNode(0) # keep adding node which value is 0 until the length of two ListNode is same.
            elif l2.next is None and l1.next is not None:
                l2.next=ListNode(0)
            if flag==1: # this situation means the addtion of the previous two nodes is bigger than 10 
                add=l1.val+l2.val+1 # we have to add one here         
            else:
                add=l1.val+l2.val # this situation means the addtion of the previous two nodes is less than 10 
            l1=l1.next
            l2=l2.next
            if add>=10: # add two node values and the result is bigger than 10
                flag=1 # we need to add 1 when we calculate the addition of next node
                add=add-10 
            else:flag=0
            R.next=ListNode(add) # add a result node at the end of result ListNode
            R=R.next
            if l1 is None and l2 is None and flag is 1: # it means the addition of last two nodes is higher than 10 and we have to extend the length of result ListNode
                R.next=ListNode(1) 
        return head.next # get rid of the head node which we create as 0
print_ListNode(l1_1)
print_ListNode(l1_2)
print_ListNode(solution().addTwoNumbers(l1_1,l1_2))
print_ListNode(l2_1)
print_ListNode(l2_2)
print_ListNode(solution().addTwoNumbers(l2_1,l2_2))
print_ListNode(l3_1)
print_ListNode(l3_2)
print_ListNode(solution().addTwoNumbers(l3_1,l3_2))