class ListNode:
    def __init__(self, data, next=None):
        self.val=data
        self.next=next
def make_ListNode(elements):
    head=ListNode(elements[0]) #將list中的第一個element建立一個起始的Node為head
    for element in elements[1:]: #從list中第二個element開始建立Node
        currentNode=head
        while currentNode.next: #代表不斷ListNode尾端移動直到最後一個時 currentNode.next=None 此時為false 跳出迴圈
            currentNode=currentNode.next
        currentNode.next=ListNode(element) #跳出迴圈後加上新的Node
    return head #返還建立完成的ListNdoe
def print_ListNode(self): # We cannot directly print the ListNode by print function, so we need to establish a function for print evey nodes from ListNode
    currentNode=head # Also, we start from the first node
    print("[", end=" ")
    while currentNode: # While currentNode is True, the loop will continue running, until the last node, the currnetNode.next will be None, then the loop halt.
        print(currentNode.val, end=" ") if currentNode.next is None else print(currentNode.val, end= ", ") # Print the values of every nodes
        currentNode=currentNode.next # move the next node
    print("]")
class solution():
    def del_ListNode(self,node,data):
        while node.next.val is not data: # while the ndoe value is not equal to data then skip it
            node=node.next # move on until the node value is equal to data
        if node.next.next is None:
            node.next=None
        else:
            node.next.val=node.next.next.val # when the node value is equal to data, replace the node value with the next value
            node.next.next=node.next.next.next # and the same time link the modified node toward the node after the next node 
head = make_ListNode([1,2,3,4,5])
print_ListNode(head)
print_ListNode(solution().del_ListNode(head,5))