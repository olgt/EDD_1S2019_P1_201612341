
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
    def __init__(self, x,y):

        

