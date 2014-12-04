from unittest import TestCase


class SimpleTestCase(TestCase):
    def test_sum(self):
        self.assertEqual(1 + 1, 2)
