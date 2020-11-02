Read items in a linked list
Update items in a linked list
Delete items in a linked list
Implement a solution to a linked list focused practice interview question

from node import Node

class Linked_List():

    def __init__(self, data_as_list=None: list):
        self.head=None
        self.tail=None
        if data_as_list != None:
            self.append_list(data_as_list)

    def append_list(self, data_as_list: list):
        for li in data_as_list:
            self.append(li)
    
    def append(self, data):
        new_node=Node(data=data)
        temp_node_rear = None
        temp_node_front = self.head
        while temp_node_front != None:
            temp_node_rear = temp_node_front
            temp_node_front = temp_node_front.get_next()
        if temp_node_rear = None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.set_last(temp_node_rear)
        self.tail = new_node

    def prepend(self, data):
        new_node=Node(data=data)
        self.insert(data, 0)

    def insert(self, data, index):
        new_node=Node(data=data)
        temp_node_rear = self.head.get_last()
        temp_node_front = self.head
        for i in index:
            temp_node_rear = temp_node_front
            temp_node_front = temp_node_front.get_next()
        temp_node_rear.set_next(new_node)
        temp_node_front.set_last(new_node)        