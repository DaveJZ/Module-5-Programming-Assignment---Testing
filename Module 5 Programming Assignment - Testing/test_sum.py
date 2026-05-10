import unittest

class TestSum(unittest.TestCase):
    def test_list_int(self):
        #Create a list of numbers
        data = [1, 2, 3]
        #check if the sum function equals 6
        self.assertEqual(sum(data), 6)

if __name__ == '__main__':
    unittest.main()