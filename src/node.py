

class Node:

    def __init__(self, data=None, next_node=None, last_node=None):
        self._data = data
        self._next_node = next_node
        self._last_node = last_node

    def set_data(self, data):
        self._data = data
    
    def get_data(self):
        return self._data

    def get_next(self):
        return self._next_node
    
    def get_last(self):
        return self._last_node

    def set_next(self, next_node):
        self._next_node = next_node
        if next_node != None:
            next_node._set_last(self)

    def set_last(self, last_node):
        self._last_node = last_node
        if last_node != None:
            last_node._set_next(self)

    def _set_next(self, next_node):
        self._next_node = next_node

    def _set_last(self, last_node):
        self._last_node = last_node