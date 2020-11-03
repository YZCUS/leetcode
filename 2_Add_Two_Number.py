class ListNode():
    def __init__(self, value):
        self.value = value
        self.next = None
    
def Createlist(n):
    if n<=0: return False
    if n==1: return ListNode(1)
    else:
        root = ListNode(1)
        temp=root
        for i in range(2,n+1):
            temp.next = ListNode(i)
            temp=temp.next
    return root

def printlist(head):
    p=head
    while p!=None:
        print(p.value,end=' ')
        p=p.next

def main():
    print("Create a linklist",end='\n')
    head=Createlist(7)
    printlist(head)

main()