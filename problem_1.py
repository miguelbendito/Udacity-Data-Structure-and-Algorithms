from collections import OrderedDict

class QNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return "(%s, %s)" % (self.key, self.value)

class LRU_Cache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """

        self.hash_map = OrderedDict()

        # No explicit doubly linked queue here
        self.head = None
        self.end = None

        self.capacity = capacity
        self.current_size = 0

    def get(self, key):
        if key not in self.hash_map:
            return -1

        node = self.hash_map[key]

        # return the value if we are already looking at head
        if self.head == node:
            return node.value
        self.remove(node)
        self.set_head(node)
        return node.value
        pass

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if self.capacity <= 0:
            print ("Cache can't be 0 or less")
            return
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value

            # update pointers only if this is not head; otherwise return
            if self.head != node:
                self.remove(node)
                self.set_head(node)
        else:
            new_node = QNode(key, value)
            if self.current_size == self.capacity:
                del self.hash_map[self.end.key]
                self.remove(self.end)
            self.set_head(new_node)
            self.hash_map[key] = new_node


    def set_head(self, node):
        if not self.head:
            self.head = node
            self.end = node
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node
        self.current_size += 1


    def remove(self, node):
        if not self.head:
            return

        # removing the node from somewhere in the middle; update pointers
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        # head = end = node
        if not node.next and not node.prev:
            self.head = None
            self.end = None

        # if the node we are removing is the one at the end, update the new end
        # also not completely necessary but set the new end's previous to be NULL
        if self.end == node:
            self.end = node.next
            self.end.prev = None
        self.current_size -= 1
        return node

    def print_elements(self):
        n = self.head
        print("[head = %s, end = %s]" % (self.head, self.end), end=" ")
        while n:
            print("%s -> " % (n), end = "")
            n = n.prev
        print("NULL")


our_cache = LRU_Cache(5)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
our_cache.print_elements()

# bad_cache = LRU_Cache(1) #cache capacity must be
case_2 = LRU_Cache(0) #cache capacity cannot be empty
case_2.set(2,2)
case_2.get(2)
case_2.print_elements()

#
case_3 = LRU_Cache(-3)
case_3.set(1,1)
case_3.get(1)
case_3.print_elements()
