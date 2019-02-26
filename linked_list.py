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

    def insert_node(self, node):
        pass


if __name__ == '__main__':

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    linklist = Linkedlist()

    linklist.head = node1
    node1.next = node2
    node2.next = node3

    print(linklist.total_list())
