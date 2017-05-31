import unittest
import credit2

class CreditTest(unittest.TestCase):

    def setUp(self):
        self.validate = validate.account_number()

    def assert_equal_rev_num(self):
        check_dig == 5
        self.assertEqual(check_dig, rev_num)  # this will fail and should fail; intended to create a failure for affirmation

    #
    #
    #
    #
    # def test_not_equal(self):
    #     self.assertNotEqual(self.rock, self.paper)


if __name__ == '__main__':
    unittest.main()
