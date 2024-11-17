class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node


    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node

    def insert_at_position(self, data, node_position):
        new_node = Node(data)
        if node_position == 1:
            self.insert_at_beginning()
        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < node_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None:
            return
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def remove_node_index(self, rm_position):
        if rm_position == 1:
            removed_node = self.head
            self.head = self.head.next_node
            print(f"Удалили: {removed_node.data}.\nТеперь начало {self.head.data}")
            return removed_node.data

        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < rm_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None or current_node.next_node is None:
            return f"Ничего не удалили\nНачало: {self.head.data}"
        removed_node = current_node.next_node
        current_node.next_node = current_node.next_node.next_node


my_cats_list = LinkedList()
my_cats_list.insert_at_end("Персик_2")
my_cats_list.insert_at_end("Барсик_3")
my_cats_list.insert_at_beginning("Феликс_1")

print(my_cats_list.head.data)
print(my_cats_list.head.next_node.data)
print(my_cats_list.head.next_node.next_node.data)
