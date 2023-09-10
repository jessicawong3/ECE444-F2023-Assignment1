import unittest

from utils import utils

# tests for reversed function
class TestReversedUtil(unittest.TestCase):
    # test if given integer
    def test_int_case(self):
        util = utils()
        self.assertEqual(util.reversed(123), 321)

    # test if given string
    def test_string_case(self):
        util = utils()
        self.assertEqual(util.reversed("123"), -1)

    # test if given float
    def test_float_case(self):
        util = utils()
        self.assertEqual(util.reversed(1.23), -1)



# tests for formatter function
class TestFormatterUtil(unittest.TestCase):
    # test if given integer
    def test_int_case(self):
        util = utils()
        self.assertEqual(util.formatter(123), ('0b1111011','0o173'))

    # test if given string
    def test_string_case(self):
        util = utils()
        self.assertEqual(util.formatter("123"), -1)

    # test if given float
    def test_float_case(self):
        util = utils()
        self.assertEqual(util.formatter(1.23), -1)



unittest.main()