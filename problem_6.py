class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current

    def duplicate(self):
        copy = LinkedList()
        current = self.head
        while current:
            node = Node(current.value)
            copy.insert_at_end(node)
            current = current.next
        return copy

    def insert_at_end(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def remove(self, node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next


def remove_duplicates(llist):
    current1 = llist.head
    while current1:
        current2 = current1.next
        data = current1.value
        while current2:
            temp = current2
            current2 = current2.next
            if temp.value == data:
                llist.remove(temp)
        current1 = current1.next

def union(llist1, llist2):
    if llist1.head is None and llist2.head is None:
        return "empty list"
    if llist1.head is None:
        union = llist2.duplicate()
        remove_duplicates(union)
        return union
    if llist2.head is None:
        union = llist1.duplicate()
        remove_duplicates(union)
        return union
    union = llist1.duplicate()
    last_node = union.head
    while last_node.next is not None:
        last_node = last_node.next
    llist2_copy = llist2.duplicate()
    last_node.next = llist2_copy.head
    remove_duplicates(union)

    # return "Empty list"
    return union


def intersection(llist1, llist2):
    if (llist1.head is None or llist2.head is None):
        return "empty lists"

    intersection = LinkedList()
    current1 = llist1.head
    while current1:
        current2 = llist2.head
        value = current1.value
        while current2:
            if current2.value == value:
                node = Node(value)
                intersection.insert_at_end(node)
                break
            current2 = current2.next
        current1 = current1.next
    remove_duplicates(intersection)
    if intersection.size() == 0:
        return "empty list"

    return intersection

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

linkedlist_5 = LinkedList()
linkedlist_6 = LinkedList()

print (union(linkedlist_5,linkedlist_6))
print (intersection(linkedlist_5,linkedlist_6))
