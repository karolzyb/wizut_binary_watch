import unittest
from binary_gpio_operations import *
from get_time import *
from print_outs import *
from safety_check import *

param_list_01 = [
       (12, 4, [1,1,0,0]),
       (4, 4, [0,1,0,0]),
       (5, 3, [1,0,1]),
       (8, 5, [0,1,0,0,0])
   ]

param_list_02 = (
    {'case': '01', 'param01': 12, 'param02': 4, 'expected': [1,1,0,0]},
    {'case': '02', 'param01': 4, 'param02': 4, 'expected': [0,1,0,0]},
    {'case': '03', 'param01': 5, 'param02': 3, 'expected': [1,0,1]},
    {'case': '04', 'param01': 8, 'param02': 5, 'expected': [0,1,0,0,0]},
    )

class Tests_binary(unittest.TestCase):
    def test_001_binary(self):
        actual_result = int_to_bin_list(12, 4)
        self.assertEqual(actual_result, [1,1,0,0])

    def test_002_binary(self):
        with self.subTest():
            self.assertEqual(int_to_bin_list(12, 4), [1,1,0,0])

    def test_003_binary(self):
        for p1, p2, p3 in param_list_01:
            with self.subTest():
                self.assertEqual(int_to_bin_list(p1, p2), p3)

    def test_004_binary(self):
        for item in param_list_02:
            with self.subTest(item['case']):
                actual_result = int_to_bin_list(item['param01'], item['param02'])
                self.assertEqual(actual_result, item['expected'])


class Tests_safety(unittest.TestCase):
    def test_001_safety(self):
        with self.assertRaises(SystemExit) as cm:
            safety_check([None, "a"])
        self.assertEqual(cm.exception.code, "Arg other than digits")

    def test_002_safety(self):
        with self.assertRaises(SystemExit) as cm:
            safety_check([None, "2.35"])
        self.assertEqual(cm.exception.code, "Arg other than digits")

    def test_003_safety(self):
        with self.assertRaises(SystemExit) as cm:
            safety_check([None, "-13"])
        self.assertEqual(cm.exception.code, "Int out of the scope")

    def test_004_safety(self):
        with self.assertRaises(SystemExit) as cm:
            safety_check([None, "#"])
        self.assertEqual(cm.exception.code, "Arg other than digits")

    def test_005_safety(self):
        with self.assertRaises(SystemExit) as cm:
            safety_check([None, "a", "2"])
        self.assertEqual(cm.exception.code, "Too many args")

    def test_006_safety(self):
        actual_result = safety_check([None, "2"])
        self.assertEqual(actual_result, None)

    def test_007_safety(self):
        actual_result = safety_check([None, "-12"])
        self.assertEqual(actual_result, None)

    def test_008_safety(self):
        actual_result = safety_check([None])
        self.assertEqual(actual_result, None)


class Tests_time(unittest.TestCase):
    def test_001_time(self):
        actual_result = get_time([None])
        expected_result = (time.gmtime().tm_hour, time.gmtime().tm_min, time.gmtime().tm_sec)
        self.assertEqual(actual_result, expected_result)