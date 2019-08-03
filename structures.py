
import os

#Node for players Structure
class playerNode:
        def _init_(self, playerName):
            self.playerName = playerName
            self.next = None
            self.previous = None

#Circular Double Linked List (uses the Node structure)
class userSeletionList:
    def __init__(self):
        self.head = None

    def __add__(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            head = self.head
            temp = self.head
            while temp.next is not head:
                temp = temp.next
            temp.next = newNode
            newNode.next = head
            newNode.previous = temp

#Node for score Structure
class pointNode:
    def __init__(self, x,y, value):
        self.head = None
        self.next = None
        self.x = x
        self.y = y
        self.value = value

#Stack linked list (Uses pointNode Structure)
class scoreList:
    def _push_(self, newNode): #Method to push a new node to stack
        if self.head is None:
            self.head = newNode
        else:
            head = self.head
            temp = self.head

            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def __pop__(self): #Method to pop last entry
        temp = self.head

        while temp.next is not None:
            tempBehind = temp
            temp = temp.next

        temp = None
        tempBehind.next = None

#Node for scoreboard players/score
class scoreBoardNode:
    def __init__(self, playerNode, score):
        self.playerNode = playerNode
        self.score = score
        self.next = None
        self.head = None

#Queue Linked list (uses scoreBoardNode)
class scoreBoardLinkedList:
    def _enqueue_(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            head = self.head
            temp = self.head

            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def _dequeue_(self): #removes the first entry
        head = self.head
        temp = head.next

        head = None
        self.head = temp








