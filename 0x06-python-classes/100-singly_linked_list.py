#!/usr/bin/python3
"""Represents an square."""


class Node:
    """Represents an square."""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if type(data) != int:
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) != Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents an square."""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            new_node = Node(value)
            self.__head = new_node
        elif self.__head.data > value:
            new_node = Node(value, self.__head)
            self.__head = new_node
        else:
            temp = self.__head
            while temp.next_node is not None:
                if temp.next_node.data > value:
                    new_node = Node(value, temp.next_node)
                    temp.next_node = new_node
                    return
                temp = temp.next_node
            if temp.next_node is None:
                new_node = Node(value)
                temp.next_node = new_node

    def __str__(self):
        temp = self.__head
        msg = ""
        while temp is not None:
            if temp.next_node is None:
                msg += str(temp.data)
            else:
                msg += str(temp.data) + "\n"
            temp = temp.next_node
        return msg
