from nose.tools import assert_equal
from nose.tools import raises


class Stacks(object):

    def __init__(self, num_stacks, stack_size):
        self.num_stacks = num_stacks
        self.stack_size = stack_size
        self.tops = []
        self.stacks = []
        self.nexts = []
        self.NO_VALUE = -1
        self.NO_NEXT = -2
        for _ in range(num_stacks):
            self.tops.append(None)
        for _ in range(stack_size):
            self.nexts.append(None)
            self.stacks.append(None)
        self.current_size = 0

    def abs_index(self, statck_index):
        return self.tops[statck_index]

    def push(self, stack_index, data):
        if self.current_size == self.stack_size:
            raise Exception
        for index, value in enumerate(self.stacks):
            if value == None:
                self.stacks[index] = data
                self.current_size += 1
                break
        if self.tops[stack_index] is not None:
            self.nexts[index] = self.tops[stack_index]
            self.tops[stack_index] = index
        else:
            self.tops[stack_index] = index
        

    def pop(self, stack_index):
        if self.current_size == 0:
            raise Exception
        if self.tops[stack_index] is None:
            raise Exception
        data = self.stacks[self.tops[stack_index]]
        self.stacks[self.tops[stack_index]] = None
        self.tops[stack_index] = self.nexts[self.tops[stack_index]]
        self.current_size -= 1
        return data
        


class TestStacks(object):

    @raises(Exception)
    def test_pop_on_empty(self, num_stacks, stack_size):
        print('Test: Pop on empty stack')
        stacks = Stacks(num_stacks, stack_size)
        stacks.pop(0)

    @raises(Exception)
    def test_push_on_full(self, num_stacks, stack_size):
        print('Test: Push to full stack')
        stacks = Stacks(num_stacks, stack_size)
        for i in range(0, stack_size):
            stacks.push(2, i)
        stacks.push(2, stack_size)

    def test_stacks(self, num_stacks, stack_size):
        print('Test: Push to non-full stack')
        stacks = Stacks(num_stacks, stack_size)
        stacks.push(0, 1)
        stacks.push(0, 2)
        stacks.push(1, 3)
        stacks.push(2, 4)

        print('Test: Pop on non-empty stack')
        assert_equal(stacks.pop(0), 2)
        assert_equal(stacks.pop(0), 1)
        assert_equal(stacks.pop(1), 3)
        assert_equal(stacks.pop(2), 4)

        print('Success: test_stacks\n')


def main():
    num_stacks = 3
    stack_size = 100
    test = TestStacks()
    test.test_pop_on_empty(num_stacks, stack_size)
    test.test_push_on_full(num_stacks, stack_size)
    test.test_stacks(num_stacks, stack_size)


if __name__ == '__main__':
    main()