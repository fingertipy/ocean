from basic.func import desc
import unittest

class AssembleTest(unittest.TestCase):
    def test_assemble(self):
        format_name = desc('cat')
        print(format_name)
        self.assertEqual(format_name, 'cat is so beautiful')

unittest.main()