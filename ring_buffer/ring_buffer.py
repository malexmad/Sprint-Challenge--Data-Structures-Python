from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            print("1")
            return self.storage.add_to_tail(item)

        elif self.storage.length == self.capacity and self.current == None:
            print("2")
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.storage.head

        elif self.current.next != None:
            print("3")
            self.current.insert_after(item)
            self.current = self.current.next
            self.current.next.delete()

        else:
            print("4")
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        node = self.storage.head

        while node != self.storage.tail:
            list_buffer_contents.append(node.value)
            node = node.next
            print(list_buffer_contents)

        list_buffer_contents.append(self.storage.tail.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
