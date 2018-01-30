from nose.tools import assert_equal
from linked_list import LinkedList, Node


class MyLinkedList(LinkedList):
    def is_palindrome(self):
        if self.head is None or self.head.next is None:
            return False
        reverse = MyLinkedList()
        temp = self.head
        count = 0
        while temp is not None:
            reverse.insert_to_front(temp.data)
            temp = temp.next
            count += 1
        temp_ori = self.head
        temp_rev = reverse.head
        for _ in range(count//2):
            if temp_ori.data != temp_rev.data:
                return False
            temp_ori = temp_ori.next
            temp_rev = temp_rev.next
        return True
        


class TestPalindrome(object):

    def test_palindrome(self):
        print('Test: Empty list')
        linked_list = MyLinkedList()
        assert_equal(linked_list.is_palindrome(), False)

        print('Test: Single element list')
        head = Node(1)
        linked_list = MyLinkedList(head)
        assert_equal(linked_list.is_palindrome(), False)

        print('Test: Two element list, not a palindrome')
        linked_list.append(2)
        assert_equal(linked_list.is_palindrome(), False)

        print('Test: General case: Palindrome with even length')
        head = Node('a')
        linked_list = MyLinkedList(head)
        linked_list.append('b')
        linked_list.append('b')
        linked_list.append('a')
        assert_equal(linked_list.is_palindrome(), True)

        print('Test: General case: Palindrome with odd length')
        head = Node(1)
        linked_list = MyLinkedList(head)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.append(1)
        assert_equal(linked_list.is_palindrome(), True)

        print('Success: test_palindrome')


def main():
    test = TestPalindrome()
    test.test_palindrome()


if __name__ == '__main__':
    main()