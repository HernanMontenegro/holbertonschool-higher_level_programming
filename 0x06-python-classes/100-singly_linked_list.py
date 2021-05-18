#!/usr/bin/python3
'''Execute'''


class Node:
    '''asd'''
    __data = 0
    __next_node = None

    def __init__(self, data, next_node=None):
        '''asd'''
        self.data = data
        self.next_node = next_node

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
        if (not isinstance(value, Node) and value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    '''LINKED LIST'''

    __head = None

    def __init__(self):
        '''Init'''
        return

    def sorted_insert(self, value):
        '''ASD Mega insert sorted'''
        new_node = Node(value)
        cursor = self.__head

        # Ask if there is not head
        if (self.__head is None):
            self.__head = new_node
            return

        if (cursor.data > value):
            new_node.next_node = cursor
            self.__head = new_node
            return

        # Reach the last node
        while cursor.next_node is not None:
            if (cursor.next_node.data > value):
                new_node.next_node = cursor.next_node
                cursor.next_node = new_node
                return
            cursor = cursor.next_node

        cursor.next_node = new_node

    def __str__(self):
        '''here there is a locked kitten'''

        cursor = self.__head

        if (cursor is None):
            return ""

        while (cursor.next_node is not None):
            print("{:d}".format(cursor.data))
            cursor = cursor.next_node
        return str(cursor.data)
