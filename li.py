class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def addFront(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def addEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def addPrevNode(self, prev, data):
        if prev is None:
            print("Invalid Input")
            return
        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node

    def delFront(self):
        pass

    def NthNodeFromLast(self, n):
        temp = self.head

        length = 0
        while temp:
            length += 1
            temp = temp.next
        if length < n:
            print("Invalid")
            return
        temp = self.head
        for i in range(0, length - n):
            temp = temp.next
        print(temp.data, "Ans")

    def findlenght(self):
        temp = self.head
        lenght = 0
        while temp:
            lenght += 1
            temp = temp.next
        print(lenght)

    def printNthNode(self, n):
        lenght = 0
        temp = self.head
        while temp:
            lenght += 1
            temp = temp.next
        if n > lenght:
            print("Invalid")
        temp = self.head
        for i in range(0, lenght - n):
            temp = temp.next
        print(temp.data)

    def reverse(self):
        prev = None
        current = self.head
        nextN = current.next

        while current is not None:
            nextN = current.next
            current.next = prev

            prev = current
            current = nextN
        self.head = prev
        return self.head

    def checkPalingdrome(self):

        temp = self.head
        temp1 = self.head
        stack = []
        flag = True

        while temp:
            stack.append(temp.data)
            temp = temp.next

        while (temp1):
            i = stack.pop()
            if temp1.data == i:
                flag = True
            else:
                flag = False
                break
            temp1 = temp1.next
        return flag


hl = linkedlist()
hl.addFront(1)
hl.addFront(2)
hl.addFront(3)
hl.addFront(5)
hl.addFront(1)

# hl.NthNodeFromLast(1)
# hl.print()
# hl.findlenght()
# hl.printNthNode(3)
if hl.checkPalingdrome() is True:
    print("True")
else:
    print("False")
