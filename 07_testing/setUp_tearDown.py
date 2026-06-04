import unittest


class TestList(unittest.TestCase):

    def setUp(self):
        self.data = [1, 2, 3]

    def tearDown(self):
        self.data = None

    def test_length(self):
        self.assertEqual(len(self.data), 3)


if __name__ == "__main__":
    unittest.main()