from src.node import Node
import threading



class Linked_List():

    find_node = None

    def __init__(self, data_as_list: list = None):
        self._head=None
        self._tail=None
        self._size=0
        if data_as_list != None:
            self.append_list(data_as_list)

    def append_list(self, data_as_list: list):
        for li in data_as_list:
            self.append(li)
    
    def append(self, data):
        new_node=Node(data=data)
        temp_node_rear = None
        temp_node_front = self._head
        self._size += 1
        while temp_node_front != None:
            temp_node_rear = temp_node_front
            temp_node_front = temp_node_front.get_next()
        if temp_node_rear == None:
            self._head = new_node
            self._tail = new_node
            return
        new_node.set_last(temp_node_rear)
        self._tail = new_node

    def prepend(self, data):
        self._size += 1
        new_node=Node(data=data)
        new_node.set_last(self._head.get_last())
        new_node.set_next(self._head)
        self._head = new_node

    def insert(self, data, index: int):
        if index == 0:
            self.prepend(data)
            return
        new_node=Node(data=data)
        temp_node_rear = self._head.get_last()
        temp_node_front = self._head
        for i in range(index):
            temp_node_rear = temp_node_front
            temp_node_front = temp_node_front.get_next()
        if temp_node_rear != None:
            temp_node_rear.set_next(new_node)
        temp_node_front.set_last(new_node)
        self._size += 1

    def find(self, data):
        tail_thread = threading.Thread(target=find_recursive_tail, arg=(self._tail, data))
        head_thread = threading.Thread(target=find_recursive_tail, arg=(self._tail, data))
        tail_thread.start()
        head_thread.start()
        tail_thread.join()
        head_thread.join()
        if self.find_node:
            self.find_node = None
            return True
        return False     

    def find_recursive_tail(self, temp_node, data):
        if temp_node == None or self.find_node:
            return False
        if temp_node.get_data() == data:
            self.find_node = temp_node
            return True
        return self.find_recursive_tail(temp_node.get_last(), data)

    def find_recursive_head(self, temp_node, data):
        if temp_node == None or self.find_node:
            return False
        if temp_node.get_data() == data:
            self.find_node = temp_node
            return True
        return self.find_recursive_head(temp_node.get_next(), data)

    def delete(self, data):
        while True:
            tail_thread = threading.Thread(target=self.find_recursive_tail, args=(self._tail, data))
            head_thread = threading.Thread(target=self.find_recursive_head, args=(self._tail, data))
            tail_thread.start()
            head_thread.start()
            tail_thread.join()
            head_thread.join()
            if self.find_node:
                self.remove_by_pointer(self.find_node)
                self.find_node = None
            else:
                break
    
    def delete_from_head(self):
        self.remove_by_index(0)

    def delete_from_tail(self):
        self.remove_by_index(self._size-1)

    def get(self, index):
        return self._get_node_by_index(index)._data

    def remove_by_pointer(self, temp_node):
        self._size -= 1
        if temp_node != self._head:
            temp_node.get_last().set_next(temp_node.get_next())
            return
        elif temp_node == self._head:
            self._head = temp_node.get_next()
            temp_node.get_last().set_next(temp_node.get_next())
        elif temp_node == self._tail:
            self._tail = temp_node.get_last()
            temp_node.get_last().set_next(temp_node.get_next())            

    def clear(self):
        self._head = None
        self._tail = None
        self._size = 0

    def remove_by_index(self, index: int):
        temp_node = self.get(index)
        self._size -= 1
        temp_node.get_last().set_next(temp_node.get_next())

    #TODO FIX THIS FUCTION
    def reverse(self):
        temp_node = self._tail
        self._tail = self._head
        self._head = temp_node

        while temp_node and temp_node.get_next() != self._tail: 
            temp_node.reverse()
            temp_node = temp_node.get_next()

    def print_songs(self):
        for song in self:
            print(song)

    def _get_node_by_index(self, index: int):
        if index >= self._size:
            raise IndexError
        if index < 0:
            index = self._size + index - 1
        if index != 0 and (self._size / index) < 2:
            temp_node = self._tail
            index = self._size - index - 1
            while index > 0:
                index -= 1
                temp_node = temp_node.get_last()
            return temp_node            
        else:
            temp_node = self._head
            while index > 0:
                index -= 1
                temp_node = temp_node.get_next()
            return temp_node

    def get_size(self):
        return self._size

    def __iter__(self):
        return Linked_List_Iterator(self)

class Linked_List_Iterator:
    ''' Iterator class '''
    def __init__(self, linked_list: Linked_List):
        self._linked_list = linked_list
        self._index = 0

    def __next__(self): 
        ''''Returns the next value from team object's lists '''
        temp_node = None
        if self._index < self._linked_list._size:
            temp_node = self._linked_list._get_node_by_index(self._index)
            self._index += 1
            return temp_node.get_data()
        # End of Iteration
        raise StopIteration