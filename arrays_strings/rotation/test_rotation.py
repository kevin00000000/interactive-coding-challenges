from nose.tools import assert_equal


class Rotation(object):

    def is_substring(self, s1, s2):
        return s1.find(s2) != -1
    
    def is_rotation(self, s1, s2):
        if s1 is None or s2 is None:
            return False
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        return self.is_substring(s1+s1, s2)

    def is_rotation_multi_callsub(self, s1, s2):
        if s1 is None or s2 is None:
            return False
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        for i in range(len(s1)):
            left = s2[0:i]
            right = s2[i:]
            if self.is_substring(s1, left) and self.is_substring(s1, right):
                return True
        return False


class TestRotation(object):

    def test_rotation(self):
        rotation = Rotation()
        assert_equal(rotation.is_rotation('o', 'oo'), False)
        assert_equal(rotation.is_rotation(None, 'foo'), False)
        assert_equal(rotation.is_rotation('', 'foo'), False)
        assert_equal(rotation.is_rotation('', ''), True)
        assert_equal(rotation.is_rotation('foobarbaz', 'barbazfoo'), True)
        print('Success: test_rotation')


def main():
    test = TestRotation()
    test.test_rotation()


if __name__ == '__main__':
    main()