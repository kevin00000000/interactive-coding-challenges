from nose.tools import assert_equal, assert_raises


class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack(object):

    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        return self.top.data if self.top is not None else None

    def is_empty(self):
        return self.peek() is None


class Hanoi(object):
    def move_disks(self, num_disks, src, dest, buff):
        if src is None or dest is None or buff is None:
            raise TypeError("Stack is None")
        if src.is_empty() or num_disks == 0:
            return
        self.move_disks(num_disks-1, src, buff, dest)
        dest.push(src.pop())
        self.move_disks(num_disks-1, buff, dest, src)      


class TestHanoi(object):

    def test_hanoi(self):
        hanoi = Hanoi()
        num_disks = 3
        src = Stack()
        buff = Stack()
        dest = Stack()

        print('Test: None towers')
        assert_raises(TypeError, hanoi.move_disks, num_disks, None, None, None)

        print('Test: 0 disks')
        hanoi.move_disks(0, src, dest, buff)
        assert_equal(dest.pop(), None)

        print('Test: 1 disk')
        src.push(5)
        hanoi.move_disks(1, src, dest, buff)
        assert_equal(dest.pop(), 5)

        print('Test: 2 or more disks')
        for disk_index in range(num_disks, -1, -1):
            src.push(disk_index)
        hanoi.move_disks(num_disks, src, dest, buff)
        for disk_index in range(0, num_disks):
            assert_equal(dest.pop(), disk_index)

        print('Success: test_hanoi')


def main():
    test = TestHanoi()
    test.test_hanoi()


if __name__ == '__main__':
    main()