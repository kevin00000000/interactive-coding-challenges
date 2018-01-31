from nose.tools import assert_equal
from stack import Stack


class QueueFromStacks(object):
    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()
        self.en = True

    def shift_stacks(self, source, destination):
        while not source.is_empty():
            destination.push(source.pop())
    
    def enqueue(self, data):
        if not self.en:
            self.shift_stacks(self.dequeue_stack, self.enqueue_stack)
        self.enqueue_stack.push(data)

    def dequeue(self):
        if self.en:
            self.shift_stacks(self.enqueue_stack, self.dequeue_stack)
        return self.dequeue_stack.pop()


class TestQueueFromStacks(object):

    def test_queue_from_stacks(self):
        print('Test: Dequeue on empty stack')
        queue = QueueFromStacks()
        assert_equal(queue.dequeue(), None)

        print('Test: Enqueue on empty stack')
        print('Test: Enqueue on non-empty stack')
        print('Test: Multiple enqueue in a row')
        num_items = 3
        for i in range(0, num_items):
            queue.enqueue(i)

        print('Test: Dequeue on non-empty stack')
        print('Test: Dequeue after an enqueue')
        assert_equal(queue.dequeue(), 0)

        print('Test: Multiple dequeue in a row')
        assert_equal(queue.dequeue(), 1)
        assert_equal(queue.dequeue(), 2)

        print('Test: Enqueue after a dequeue')
        queue.enqueue(5)
        assert_equal(queue.dequeue(), 5)

        print('Success: test_queue_from_stacks')


def main():
    test = TestQueueFromStacks()
    test.test_queue_from_stacks()


if __name__ == '__main__':
    main()