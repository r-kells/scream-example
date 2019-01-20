import unittest

from company.project.module import add_1


class ExampleTest(unittest.TestCase):

    def test_example(self):
        result = add_1(1)
        self.assertTrue(result == 2)
