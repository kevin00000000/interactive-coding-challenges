from nose.tools import assert_equal
from linked_list import LinkedList, Node


class MyLinkedList(LinkedList):
    def partition(self, data):
        if self.head is None:
            return self
        less = MyLinkedList()
        more = MyLinkedList()
        equal = MyLinkedList()
        result = MyLinkedList()
        temp = self.head
        while temp is not None:
            if temp.data < data:
                less.insert_to_front(temp.data)
            elif temp.data > data:
                more.insert_to_front(temp.data)
            else:
                equal.insert_to_front(temp.data)
            temp = temp.next
        temp = more.head
        while temp is not None:
            result.insert_to_front(temp.data)
            temp = temp.next
        temp = equal.head
        while temp is not None:
            result.insert_to_front(temp.data)
            temp = temp.next
        temp = less.head
        while temp is not None:
            result.insert_to_front(temp.data)
            temp = temp.next
        self.head = result.head
        return self


class TestPartition(object):

    def test_partition(self):
        print('Test: Empty list')
        linked_list = MyLinkedList(None)
        linked_list.partition(10)
        assert_equal(linked_list.get_all_data(), [])

        print('Test: One element list, left list empty')
        linked_list = MyLinkedList(Node(5))
        linked_list.partition(0)
        assert_equal(linked_list.get_all_data(), [5])

        print('Test: Right list is empty')
        linked_list = MyLinkedList(Node(5))
        linked_list.partition(10)
        assert_equal(linked_list.get_all_data(), [5])

        print('Test: General case')
        # Partition = 10
        # Input: 4, 3, 13, 8, 10, 1, 14, 10, 12
        # Output: 4, 3, 8, 1, 10, 10, 13, 14, 12
        linked_list = MyLinkedList(Node(12))
        linked_list.insert_to_front(10)
        linked_list.insert_to_front(14)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(10)
        linked_list.insert_to_front(8)
        linked_list.insert_to_front(13)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(4)
        partitioned_list = linked_list.partition(10)
        assert_equal(partitioned_list.get_all_data(),
                     [4, 3, 8, 1, 10, 10, 13, 14, 12])

        print('Success: test_partition')


def main():
    test = TestPartition()
    test.test_partition()


if __name__ == '__main__':
    main()