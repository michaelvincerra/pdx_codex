import unittest
import main


class MainTest(unittest.TestCase):
    """
    Test string methods. 
    
    """
    # def setUp(self):
    # #     self.validate = validate.account_number()
    # def assert_equal_rev_num(self):
    #     check_dig == 5
    #     self.assertEqual(check_dig, rev_num)  # this will fail and should fail; intended to create a failure for affirmation

    def setUp(self):
        self.higher = main.Higher()
        self.middle = main.Middle()
        self.lower = main.Lower()











    # def test_five_plus_five(self):
    #     assert 5 + 5 == 10
    #
    # def test_one_plus_one(self):
    #     assert not 1 + 1 == 3
    #
    # def test_two_plus_two(self):
    #     assert not 2 + 2 == 5


    def test_upper(self):
        self.assertTrue('BOOKS'.isupper())

    def test_not_equal(self):
        self.assertNotEqual(self.higher, self.middle)

    def test_not_equal(self):
        self.assertNotEqual(self.middle, self.lower)
    #
    # def test_more_difficult(self):
    #     self.assertGreaterEqual(self.higher, self.lower)



#
# def test_ari_scale(self):
#     ari_scale == <= 14:
#     self.LesserEqual()

if __name__ == '__main__':
    unittest.main()
