from Tools.scripts.generate_opcode_h import header


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# #traversal
# temp=head
# while temp.next:
#     print(temp.data,end=' ')
#     temp=temp.next
# print(temp.data)
# #or
# temp=head
# while temp:
#     print(temp.data,end=' ')
#     temp=temp.next
#

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print(None)

    def add(self):
        sum=0
        temp=self.head
        while temp:
            if temp.data%2==0:
                sum=sum+temp.data
            temp=temp.next
        print(sum)

    def cnt(self):
        c=0
        temp=self.head
        while temp:
            c=c+1
            temp=temp.next
        print(c)

l1=LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.display()
l1.add()
l1.cnt()

#https://leetcode.com/problems/middle-of-the-linked-list/ (brute force)
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    c = 0
    temp = head
    while temp:
        c += 1
        temp = temp.next
    temp = head
    for i in range(c // 2):
        temp = temp.next
    return temp

#https://leetcode.com/problems/merge-two-sorted-lists/
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        list3 = dummy
        res = dummy
        while list1 and list2:
            if list1.val < list2.val:
                list3.next = list1
                list1 = list1.next
                list3 = list3.next
            else:
                list3.next = list2
                list2 = list2.next
                list3 = list3.next
        while list1:
            list3.next = list1
            list3 = list3.next
            list1 = list1.next
        while list2:
            list3.next = list2
            list2 = list2.next
            list3 = list3.next
        return res.next


#https://leetcode.com/problems/reverse-linked-list/
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev