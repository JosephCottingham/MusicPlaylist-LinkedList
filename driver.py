from src.linked_list import Linked_List
from randomgenius import getData

if __name__ == '__main__':
    print('##############################')
    linked_list = Linked_List()
    for x in range(5):
        linked_list.append(getData())
    print(linked_list.get_size())
    linked_list.print_songs()
    song_names = list()
    for x in range(5):
        song_names.append(getData())
    linked_list.append_list(song_names)
    print('\n\n')
    print(linked_list.get_size())
    linked_list.print_songs()
    linked_list.prepend(getData())
    print('\n\n')
    print(linked_list.get_size())
    linked_list.print_songs()  
    linked_list.insert(getData(), 3)
    print('\n\n')
    print(linked_list.get_size())
    linked_list.print_songs()
    linked_list.delete(song_names[1])
    print('\n\n')
    print(song_names[1] + " was removed")
    print(linked_list.get_size())
    linked_list.print_songs()
    linked_list.reverse()
    print('\n\n')
    print(song_names[1] + " was removed")
    print(linked_list.get_size())
    linked_list.print_songs()    

