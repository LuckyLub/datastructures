class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


class Linkedlist:

    def __init__(self):

        self.head = None

    def total_list(self):
        node = self.head
        total = str()
        while True:
            total += str(node.data)
            if node.next is not None:
                total += ", "
                node = node.next
            else:
                break
        return total

    def push(self, new_data):
        new_node = Node(new_data)
        new_node = self.head
        self.head = new_node

    @staticmethod
    def insert_after(new_data, previous_node):
        new_node = Node(new_data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    def append(self, new_data):
        if self.head is not None:
            node_ = self.head
            while node_:
                node_to_insert_after = node_
                node_ = node_.next
            Linkedlist.insert_after(new_data, node_to_insert_after)
        else:
            new_node = Node(new_data)
            self.head = new_node




if __name__ == '__main__':

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    linklist1 = Linkedlist()

    linklist1.head = node1
    node1.next = node2
    node2.next = node3

    linklist1.insert_after(5, node2)
    linklist1.insert_after(4, node1)
    linklist1.insert_after(1114, node3)
    linklist1.append(20335)

    print(linklist1.total_list())

    linklist2 = Linkedlist()
    linklist2.append(1)
    linklist2.append(2)
    linklist2.append(3)
    p

    print(linklist2.total_list())