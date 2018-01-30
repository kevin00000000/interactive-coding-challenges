from nose.tools import assert_equal
from linked_list import LinkedList, Node


class MyLinkedList(LinkedList):
    def remove_dupes(self):
        if self.head is None or self.head.next is None:
            return
        mark = set()
        temp = self.head
        last = self.head
        while temp is not None:
            if temp.data not in mark:
                mark.add(temp.data)
                last = temp
                temp = temp.next
            else:
                last.next = temp.next
                temp = temp.next


class TestRemoveDupes(object):

    def test_remove_dupes(self, linked_list):
        print('Test: Empty list')
        linked_list.remove_dupes()
        assert_equal(linked_list.get_all_data(), [])

        print('Test: One element list')
        linked_list.insert_to_front(2)
        linked_list.remove_dupes()
        assert_equal(linked_list.get_all_data(), [2])

        print('Test: General case, duplicates')
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(2)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(1)
        linked_list.remove_dupes()
        assert_equal(linked_list.get_all_data(), [1, 3, 2])

        print('Test: General case, no duplicates')
        linked_list.remove_dupes()
        assert_equal(linked_list.get_all_data(), [1, 3, 2])

        print('Success: test_remove_dupes\n')


def main():
    test = TestRemoveDupes()
    linked_list = MyLinkedList(None)
    test.test_remove_dupes(linked_list)


if __name__ == '__main__':
    main()