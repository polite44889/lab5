import unittest
from lab import Stack, get_input
from unittest.mock import Mock
from unittest.mock import patch

class TestLab(unittest.TestCase):

    def test1(self):
        s=Stack()
        s.push(1)
        self.assertEqual(s.items, [1])

    @patch('lab.get_input', return_value=Mock())
    def test2(self,get_input):
        get_input.side_effect=['1','9999']
        s = Stack()
        s.push(1)
        s.push(2)
        s.edit()
        self.assertEqual(s.items,[1,'9999'])
    def test3(self):
        s=Stack()
        s.push(1)
        s.push(2)
        s.pop()
        self.assertEqual(s.items, [1])
    def test4(self):
        s=Stack()
        s.isEmpty()
        self.assertEqual(s.items,[])
    def test5(self):
        s=Stack()
        s.push(1)
        s.push(2)
        s.push(5)
        self.assertEqual(s.peek(),5)
    def test6(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(5)
        self.assertEqual(s.size(), 3)
    def test7(self):
        s = Stack()
        try:
            s.pop()
        except IndexError:
            self.assertRaises(IndexError, s.pop)
    def test8(self):
        s = Stack()
        try:
            s.peek()
        except IndexError:
            self.assertRaises(IndexError, s.peek)
    @patch('lab.get_input', return_value=Mock())
    def test9(self, get_input):
        get_input.side_effect = ['4','9999']
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(5)
        self.assertRaises(IndexError, s.edit)


if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-repots')
    unittest.main(testRunner=runner)
    unittest.main()
