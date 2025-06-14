class Node:
    def __init__(self,value):
        self.value=value
        self.next= None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def append(self,value):
        newNode=Node(value)
        if not self.head:
            self.tail=newNode
            self.head=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode

    def prepend(self,value):
        newNode=Node(value)
        if not self.head:
            self.tail=newNode
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    
    def iterate(self):
        iterate=self.head
        while iterate:
            print(iterate.value+" ")
            iterate=iterate.next 
    
    def remove(self,value):
        if not self.head:
            return
        if not self.head.value==value:
            self.head=self.head.next
            if not self.head:
                self.tail=None
            return
        iterator=self.head
        while iterator.next:
            if iterator.next.value==value:
                iterator.next=iterator.next.next
                if not iterator.next:
                    self.tail=iterator
                return
            iterator=iterator.next