"""
==========================================
Linked List - Search Node
==========================================

This program demonstrates how to search
for a node in a Singly Linked List.

Operations:
- Insert at End
- Search by Value
- Display List
"""

from typing import Optional


class Node:
    """Represents a node in the linked list."""

    def __init__(self, data: int):
        self.data = data
        self.next: Optional["Node"] = None


class SinglyLinkedList:
    """Implementation of search operation."""

    def __init__(self):
        self.head: Optional[Node] = None

    # --------------------------------------
    # Insert at End
    # --------------------------------------

    def insert_at_end(self, data: int) -> None:

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    # --------------------------------------
    # Search by Value
    # --------------------------------------

    def search(self, value: int) -> None:

        current = self.head
        position = 1

        while current:

            if current.data == value:
                print(
                    f"Value {value} found at position {position}."
                )
                return

            current = current.next
            position += 1

        print(f"Value {value} not found in the linked list.")

    # --------------------------------------
    # Display Linked List
    # --------------------------------------

    def display(self) -> None:

        if self.head is None:
            print("Linked List is empty.")
            return

        current = self.head

        print("\nLinked List:")

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# ------------------------------------------
# Main Program
# ------------------------------------------

def main():

    linked_list = SinglyLinkedList()

    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(40)
    linked_list.insert_at_end(50)

    linked_list.display()

    print()

    linked_list.search(30)
    linked_list.search(100)


if __name__ == "__main__":
    main()

#Expected Output


Linked List:
10 -> 20 -> 30 -> 40 -> 50 -> None

Value 30 found at position 3.
Value 100 not found in the linked list.
