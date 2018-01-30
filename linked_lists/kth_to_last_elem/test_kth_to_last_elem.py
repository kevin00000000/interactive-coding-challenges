from nose.tools import assert_equal
from linked_list import LinkedList, Node


class MyLinkedList(LinkedList):
    def kth_to_last_elem(self, k):
        if self.head is None:
            return None
        x = 0
        odd = True
        slow = self.head
        fast = self.head
        while fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            x += 1
            if fast is None:
                odd = False
                break
        if odd:
            count = 2*x+1
        else:
            count = 2*x
        if k+1>count:
            return None
        if count-k-1>x:
            while count-k-1>x:
                slow = slow.next
                x+=1
        elif count-k-1<x:
            slow = slow.head
            x = 0
            while x<count-k-1:
                slow = slow.next
                x += 1
        return slow.data


class MyLinkedList_solution(LinkedList):
    def kth_to_last_elem(self, k):
        if self.head is None:
            return None
        slow = self.head
        fast = self.head
        for _ in range(k):
            fast = fast.next
            if fast is None:
                return None
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        return slow.data

class Test(object):

    def test_kth_to_last_elem(self):
        print('Test: Empty list')
        linked_list = MyLinkedList(None)
        assert_equal(linked_list.kth_to_last_elem(0), None)

        print('Test: k >= len(list)')
        assert_equal(linked_list.kth_to_last_elem(100), None)

        print('Test: One element, k = 0')
        head = Node(2)
        linked_list = MyLinkedList(head)
        assert_equal(linked_list.kth_to_last_elem(0), 2)

        print('Test: General case')
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(5)
        linked_list.insert_to_front(7)
        assert_equal(linked_list.kth_to_last_elem(2), 3)

        print('Success: test_kth_to_last_elem')


def main():
    test = Test()
    test.test_kth_to_last_elem()


if __name__ == '__main__':
    main()