from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print(self):
        if self.head is None:
            print("LL is empty!")
            return

        ptr = self.head
        while ptr is not None:
            print(ptr.value)
            ptr = ptr.next

    def append(self, value):
        node = Node(value)
        self.length += 1

        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def prepend(self, value):
        node = Node(value)
        ptr = self.head
        self.head = node
        self.head.next = ptr
        self.length += 1

        if self.length == 1:
            self.tail = self.head

    def pop(self):
        """ Pop last node """
        prev_ptr = self.head
        ptr = self.head

        # Traverse till the end of LL to get last node
        # prev_ptr points to last but one node
        # ptr points to last node
        while ptr is not None and ptr.next:
            prev_ptr = ptr
            ptr = ptr.next

        if prev_ptr is None:
            print("Linked List is empty. Nothing to pop!")
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return ptr.value
        else:
            prev_ptr.next = None
            self.tail = prev_ptr
            self.length -= 1
            return ptr.value

    def pop_first(self):
        ptr = self.head
        if self.head is None:
            print("Linked List is empty. Nothing to pop first!")
            return None
        elif self.head == self.tail:
            self.tail = self.head.next

        self.head = self.head.next
        self.length -= 1
        return ptr.value

    def get(self, index):
        """Returns the node's value at passed index"""
        if index >= self.length or index < 0:
            print(f"Passed an invalid index: {index}")
            return None

        ptr = self.head
        if ptr is None:
            print("Linked List is empty.")
            return None

        for _ in range(index):
            ptr = ptr.next

        return ptr.value

    def set(self, index, value):
        """Sets value of a node at given index"""
        if index < 0 or index >= self.length:
            print(f"Passed an invalid index: {index}")
            return False

        ptr = self.head

        for _ in range(index):
            ptr = ptr.next

        ptr.value = value
        return True

    def insert(self, index, value):
        """Insert a node of given value at a given index"""
        if index < 0 or index > self.length:
            print(f"Passed an invalid index: {index}")
            return False

        if index == 0:
            self.prepend(value)
            return True
        else:
            ptr = prev_ptr = self.head
            node = Node(value)

            for _ in range(index):
                prev_ptr = ptr
                ptr = ptr.next

            prev_ptr.next = node
            node.next = ptr
            self.length += 1
            return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            print(f"Passed an invalid index: {index}")
            return False

        ptr = prev_ptr = self.head
        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
                self.length = 0
            else:
                self.head = self.head.next
        else:
            for _ in range(index):
                prev_ptr = ptr
                ptr = ptr.next

            prev_ptr.next = ptr.next
            self.length -= 1

        return True

    def reverse(self):
        """Reverse a Linked List"""
        if self.head is None:
            print("Linked List is empty, thus it can't be reversed!")
            return False

        ptr = self.head

        # Swap head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp

        # Take 3 pointers before, ptr, after
        # reverse direction of "ptr.next" each time in the loop
        before = None
        while ptr.next:
            after = ptr.next
            ptr.next = before
            before = ptr
            ptr = after
        ptr.next = before
        return True
