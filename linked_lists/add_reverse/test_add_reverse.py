from nose.tools import assert_equal
from linked_list_k import LinkedList, Node


class MyLinkedList_iter(LinkedList):
    def __init__(self, head=None):
        super().__init__(head)
    
    def add_reverse(self, first_list, second_list):
        if first_list is None or second_list is None:
            return None 
        temp_first = first_list.head
        temp_second = second_list.head
        carry = []
        result = LinkedList()
        while temp_first is not None or temp_second is not None:
            first_num = temp_first.data if temp_first is not None else 0
            second_num = temp_second.data if temp_second is not None else 0
            result.append((first_num+second_num) % 10)
            carry.append((first_num+second_num) // 10)
            temp_first = temp_first.next_node if temp_first else None
            temp_second = temp_second.next_node if temp_second else None
        if len(result) == 0:
            return result
        temp = result.head.next_node
        index = 0
        while temp is not None:
            temp.data = temp.data + carry[index]
            if temp.data == 10:
                carry[index+1] += 1
                temp.data = temp.data % 10
            index += 1
            temp = temp.next_node
        if carry[index] == 1:
            result.append(1)
        return result


class MyLinkedList(LinkedList):
    def add_reverse(self, first_list, second_list):
        if first_list is None or second_list is None:
            return None
        carry = 0
        head = self._add_reverse(first_list.head, second_list.head, carry)
        return LinkedList(head)

    def _add_reverse(self, first_node, second_node, carry):
        if first_node is None and second_node is None and not carry:
            return None
        first_num = first_node.data if first_node is not None else 0
        second_num = second_node.data if second_node is not None else 0
        node = Node((first_num+second_num+carry)%10)
        carry = (first_num + second_num+carry)//10
        first_node = first_node.next_node if first_node is not None else None
        second_node = second_node.next_node if second_node is not None else None
        node.next_node = self._add_reverse(first_node, second_node, carry)
        return node




class TestAddReverse(object):

    def test_add_reverse(self):
        print('Test: Empty list(s)')
        assert_equal(MyLinkedList().add_reverse(None, None), None)
        assert_equal(MyLinkedList().add_reverse(Node(5), None), None)
        assert_equal(MyLinkedList().add_reverse(None, Node(10)), None)

        print('Test: Add values of different lengths')
        # Input 1: 6->5->None
        # Input 2: 9->8->7
        # Result: 5->4->8
        first_list = MyLinkedList(Node(6))
        first_list.append(5)
        second_list = MyLinkedList(Node(9))
        second_list.append(8)
        second_list.append(7)
        result = MyLinkedList().add_reverse(first_list, second_list)
        assert_equal(result.get_all_data(), [5, 4, 8])

        print('Test: Add values of same lengths')
        # Input 1: 6->5->4
        # Input 2: 9->8->7
        # Result: 5->4->2->1
        first_head = Node(6)
        first_list = MyLinkedList(first_head)
        first_list.append(5)
        first_list.append(4)
        second_head = Node(9)
        second_list = MyLinkedList(second_head)
        second_list.append(8)
        second_list.append(7)
        result = MyLinkedList().add_reverse(first_list, second_list)
        assert_equal(result.get_all_data(), [5, 4, 2, 1])

        print('Success: test_add_reverse')


def main():
    test = TestAddReverse()
    test.test_add_reverse()


if __name__ == '__main__':
    main()