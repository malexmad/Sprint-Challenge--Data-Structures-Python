class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    # [5,4,3,2,1]
    def reverse_list(self, node, prev):
        # You must use recursion for this solution

        # if sll is empty return None
        if node == None:
            return None

        # (Base Case) if the next node is none it is the end of the sll and change it to head
        if node.next_node == None:
            self.head = node
            return

        # run the reverse method until base case is reached
        self.reverse_list(node.next_node, node)

        # (1), head
        # 2->1=> (2),  3->2=> (3),  4->3=> (4),  5->4=> (5), reversing setting next node
        node.next_node.set_next(node)
        # 2 ->1 => 3,  3 ->2 => 4,  4->3=>5,  5->4=>None, next node needs to be the prev
        node.next_node = prev

        # while node != None:
        #     next = node.next_node  #4
        #     node.next_node = prev # none
        #     prev = node  # 5
        #     node = next  # 4
        # self.head = prev
        #
        # if node == None:
        #     return node

# list1 = LinkedList()
# list1.add_to_head(1)
# list1.add_to_head(2)
# list1.add_to_head(3)
# list1.add_to_head(4)
# list1.add_to_head(5)
# # [5,4,3,2,1]
# list1.reverse_list(list1.head, None)
# print(list1.head.value)
# print(list1.head.next_node.value)
# print(list1.head.next_node.next_node.next_node.next_node.next_node)
# [1,2,3,4,5]
