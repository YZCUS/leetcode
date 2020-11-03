class ListNode():
    def __init__(self, value):
        self.value = value
        self.next = None
    
def Createlist(n):    #創建節點
    if n<=0: return False
    if n==1: return ListNode(1)
    else:
        root = ListNode(1)
        temp=root
        for i in range(2,n+1):
            temp.next = ListNode(i)
            temp=temp.next
    return root

def printlist(head):     #列印鍵表
    p=head
    while p!=None:
        print(p.value,end=' ')
        p=p.next

def listlen(head):        #鍵表長度
    c=0
    p=head
    while p!=None:
        p=p.next
        c+=1
    return c

def insert(head,n):
    if n<1 or n>listlen(head):
        return
    p=head
    for i in range(1,n-1):
        p=p.next
    a=raw_input("Enter a value:")
    t=ListNode(value=a)
    t.next=p.next
    p.next=t
    return head

def main():      #主函數
    print("Create a linklist",end='\n')
    head=Createlist(7)
    printlist(head)
    print("The length of listnode is ",listlen(head))


main()       #執行主函數