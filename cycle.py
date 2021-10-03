class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class list:
    def __init__(self):
        self.head = None

    def insertFront(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def checkCycle(self):
        fast = self.head
        slow = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                self.remove(slow)
        return False

    def removeFront(self):
        first = self.head
        if first is None:
            return
        self.head = first.next
        return

    def remove(self, slow):
        ptr1 = slow
        ptr2 = slow
        k = 1
        while ptr2.next != ptr1:
            ptr2 = ptr2.next
            k += 1
        ptr1 = self.head
        ptr2 = self.head
        for i in range(k):
            ptr2 = ptr2.next
        while ptr2.next != ptr1:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr2.next = None

    def removeLast(self):
        temp = self.head
        if temp is None:
            return
        if temp.next is None:
            self.head = None
            return
        second_node = temp
        while second_node.next.next:
            second_node = second_node.next
        second_node.next = None
        return

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def reverse(self):
        current = self.head
        prev = None

        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp


ob = list()
ob.insertFront(5)
ob.insertFront(6)
ob.insertFront(9)
z = ob.checkCycle()
ob.reverse()
ob.print()
# if z is True:
#     print("Cycle")
# else:
#     print("Not Cycle Presnet")
