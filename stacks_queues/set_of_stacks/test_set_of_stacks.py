from nose.tools import assert_equal
from stack import Stack,Node


class StackWithCapacity(Stack):

    def __init__(self, top=None, capacity=10):
        super().__init__(top)
        self.capacity = capacity
        self.size = 0
        if self.size > capacity:
            raise Exception

    def push(self, data):
        if self.size < self.capacity:
            self.size += 1
            super().push(data)
            return True
        else:
            return False

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return super().pop()
        else:
            return None

    def is_full(self):
        return self.size == self.capacity


class SetOfStacks(object):
    def __init__(self, indiv_stack_capacity):
        self.capacity = indiv_stack_capacity
        self.stacks = []
        
    def push(self, data):
        if len(self.stacks) == 0:
            stack = StackWithCapacity(None, self.capacity)
            stack.push(data)
            self.stacks.append(stack)
            return
        stack = self.stacks[len(self.stacks)-1]
        if not stack.push(data):
            stack = StackWithCapacity(None, self.capacity)
            stack.push(data)
            self.stacks.append(stack)
    
    def pop(self):
        if len(self.stacks) == 0:
            return None
        stack = self.stacks[len(self.stacks)-1]
        data = stack.pop()
        if data is None:
            self.stacks.pop()
            if len(self.stacks) > 0:
                stack = self.stacks[len(self.stacks)-1]
                data = stack.pop()
        return data


class TestSetOfStacks(object):

    def test_set_of_stacks(self):
        print('Test: Push on an empty stack')
        stacks = SetOfStacks(indiv_stack_capacity=2)
        stacks.push(3)

        print('Test: Push on a non-empty stack')
        stacks.push(5)

        print('Test: Push on a capacity stack to create a new one')
        stacks.push('a')

        print('Test: Pop on a stack to destroy it')
        assert_equal(stacks.pop(), 'a')

        print('Test: Pop general case')
        assert_equal(stacks.pop(), 5)
        assert_equal(stacks.pop(), 3)

        print('Test: Pop on no elements')
        assert_equal(stacks.pop(), None)

        print('Success: test_set_of_stacks')


def main():
    test = TestSetOfStacks()
    test.test_set_of_stacks()


if __name__ == '__main__':
    main()