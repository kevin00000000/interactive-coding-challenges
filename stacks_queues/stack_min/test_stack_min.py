from nose.tools import assert_equal
from stack import Stack
import sys


class StackMin(Stack):
    def __init__(self, top=None):
        super().__init__(top)
        self.min_stack = Stack()
        self.cur_min = sys.maxsize
    
    def minimum(self):
        if self.is_empty():
            return sys.maxsize
        return self.cur_min

    def push(self, data):
        super().push(data)
        if data < self.cur_min:
            self.min_stack.push(data)
            self.cur_min = data
        else:
            self.min_stack.push(self.cur_min)

    def pop(self):
        self.min_stack.pop()
        self.cur_min = self.min_stack.peek()
        return super().pop()


class TestStackMin(object):

    def test_stack_min(self):
        print('Test: Push on empty stack, non-empty stack')
        stack = StackMin()
        stack.push(5)
        assert_equal(stack.peek(), 5)
        assert_equal(stack.minimum(), 5)
        stack.push(1)
        assert_equal(stack.peek(), 1)
        assert_equal(stack.minimum(), 1)
        stack.push(3)
        assert_equal(stack.peek(), 3)
        assert_equal(stack.minimum(), 1)
        stack.push(0)
        assert_equal(stack.peek(), 0)
        assert_equal(stack.minimum(), 0)

        print('Test: Pop on non-empty stack')
        assert_equal(stack.pop(), 0)
        assert_equal(stack.minimum(), 1)
        assert_equal(stack.pop(), 3)
        assert_equal(stack.minimum(), 1)
        assert_equal(stack.pop(), 1)
        assert_equal(stack.minimum(), 5)
        assert_equal(stack.pop(), 5)
        assert_equal(stack.minimum(), sys.maxsize)

        print('Test: Pop empty stack')
        assert_equal(stack.pop(), None)

        print('Success: test_stack_min')


def main():
    test = TestStackMin()
    test.test_stack_min()


if __name__ == '__main__':
    main()