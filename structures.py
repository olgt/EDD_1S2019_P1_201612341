
import os
import curses
import subprocess
import pydot

#Node for players Structure
class playerNode:
        def __init__(self, playerName):
            self.playerName = playerName
            self.next = None
            self.prev = None

#Circular Double Linked List (uses the Node structure)
class userSeletionList:
    def __init__(self):
        self.head = None

    def add(self, user_name):
        if self.head is None:
            newPlayerNode = playerNode(user_name)
            newPlayerNode.prev = None
            self.head = newPlayerNode
        else:
            newPlayerNode = playerNode(user_name)
            head = self.head
            temp = self.head
            while temp.next and temp.next is not head:
                temp = temp.next
            temp.next = newPlayerNode
            newPlayerNode.next = head
            newPlayerNode.prev = temp
            self.head.prev = newPlayerNode

    # Generates double linked list
    def generate_graphviz(self):
        if self.head is None:
            print('The list is Empty')
        else:
            f = open('UsersReport.dot', 'w')
            f.write('digraph firstGraph{\n')
            f.write('node [shape = record];\n')
            f.write('rankdir=LR;\n')
            temp = self.head
            count = 0

            while temp.next is not None and temp.next is not self.head:
                f.write('node{} [label=\" {} \"];\n'.format(count, str(temp.playerName)))
                count += 1
                f.write('node{} -> node{};\n'.format(count - 1, count))
                temp = temp.next

            # print(temp.id)
            f.write('node{} [label=" {} \"];\n'.format(count, str(temp.playerName)))
            f.write('}')
            f.close()
            os.system('dot UsersReport.dot -Tpng -o UsersReport.png')
            try:
                os.startfile('UsersReport.png')
                subprocess.check_call(['open', 'UsersReport.png'])
            except:
                print('Error')


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
    def push(self, newNode): #Method to push a new node to stack
        if self.head is None:
            self.head = newNode
        else:
            head = self.head
            temp = self.head

            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def pop(self): #Method to pop last entry
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
    def enqueue(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            head = self.head
            temp = self.head

            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def dequeue(self): #removes the first entry
        head = self.head
        temp = head.next

        head = None
        self.head = temp

#Node for Snake

class snake_Node:
    def __init__(self, value, x, y):
        self.value = value
        self.y = y
        self.x = x
        self.head = None
        self.prev = None
        self.next = None

#Double Linked list for the Snake
class snake_Structure:
    def __init__(self):
        self.head = None

    def addPoint(self, value, x, y):
        newSnakeNode = snake_Node(value,x,y)
        if self.head is None:
            self.head = newSnakeNode
            newSnakeNode.next = None
            newSnakeNode.prev = None
        else:
            temp = self.head
            while temp.next and temp.next is not None:
                temp = temp.next
            newSnakeNode.prev = temp
            temp.next = newSnakeNode

    def addPointAndChangeHead(self, value, x, y):
        newSnakeNode = snake_Node(value, x, y)

        temp = self.head

        newSnakeNode.next = temp
        newSnakeNode.prev = None

        temp.prev = newSnakeNode

        self.head = newSnakeNode

    def removePoint(self):
        temp = self.head
        tempPrev = self.head

        while temp.next and temp.next is not None:
            temp = temp.next
            tempPrev = temp.prev
        temp = None
        tempPrev.next = None

    def passingThroughPoint(self, character, x, y):
        snakePoint = snake_Node(character, x, y)

        if character is '+':
            self.addPoint(snakePoint)
        elif character is '*':
            self.removePoint()

    def drawNodes(self, screen, x, y):
        temp = self.head

        while temp.next:
            screen.addstr(temp.y, temp.x, '#')
            temp = temp.next





