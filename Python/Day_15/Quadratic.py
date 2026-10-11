class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def insert(self, head, data):
        new_node = Node(data)

        if head is None:
            return new_node

        current = head
        while current.next is not None:
            current = current.next

        current.next = new_node
        return head


if __name__ == '__main__':
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        sys.exit()

    n = int(data[0])
    values = list(map(int, data[1:1 + n]))

    head = None
    mylist = Solution()

    for value in values:
        head = mylist.insert(head, value)

    mylist.display(head)
