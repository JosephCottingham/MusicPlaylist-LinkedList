from src.linked_list import Linked_List
from randomgenius import getData

if __name__ == '__main__':
    linked_list = Linked_List()
    for x in range(25):
        linked_list.append(getData())
    linked_list.print_songs()