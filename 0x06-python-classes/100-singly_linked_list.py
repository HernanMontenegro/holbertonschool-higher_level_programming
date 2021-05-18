#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if (not isinstance(value, int)):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if (not isinstance(value, Node) and value != None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    head = None

    def __init__(self):
        pass
    
    def sorted_insert(self, value):
        new_node = Node(value)
        cursor = SinglyLinkedList.head

        # Ask if there is not head
        if (not SinglyLinkedList.head):
            SinglyLinkedList.head = new_node
            return

        # Reach the last node
        while cursor != None:
            if (value < 0 and cursor.data < 0):
                if (value > cursor.data):
                    SinglyLinkedList.head = new_node
                    new_node.next_node = cursor
                    return
            elif (value >= 0 and cursor.data >= 0):
                if (value > cursor.data):
                    cursor.next_node = new_node
                    return
            cursor = cursor.next_node
        
        

    def __str__(self):
        cursor = SinglyLinkedList.head

        while (cursor.next_node != None):
            print("{:d}".format(cursor.data))
            cursor = cursor.next_node
        return str(cursor.data)
