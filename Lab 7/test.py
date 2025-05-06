import unittest

from Solver import *
from test_data import *

class TestStringMethods(unittest.TestCase):

    def test_task1(self):
        self.assertEqual(solve_task1(input_file=input_task1_test1, write2file=False, read_from_file=False), expectet_output_t1t1)
        self.assertEqual(solve_task1(input_file=input_task1_test2, write2file=False, read_from_file=False), expectet_output_t1t2)
        self.assertEqual(solve_task1(input_file=input_task1_test3, write2file=False, read_from_file=False), expectet_output_t1t3)
        self.assertEqual(solve_task1(input_file=input_task1_test4, write2file=False, read_from_file=False), expectet_output_t1t4)
        self.assertEqual(solve_task1(input_file=input_task1_test5, write2file=False, read_from_file=False), expectet_output_t1t5)
        self.assertIsNotNone(solve_task1(input_file=input_task1_test6, write2file=False, read_from_file=False))
        
    def test_task2(self):
        self.assertEqual(solve_task2(input_file=input_task2_test1, write2file=False, read_from_file=False), expectet_output_t2t1)
        self.assertEqual(solve_task2(input_file=input_task2_test2, write2file=False, read_from_file=False), expectet_output_t2t2)
        self.assertEqual(solve_task2(input_file=input_task2_test3, write2file=False, read_from_file=False), expectet_output_t2t3)
        self.assertEqual(solve_task2(input_file=input_task2_test4, write2file=False, read_from_file=False), expectet_output_t2t4)
        self.assertEqual(solve_task2(input_file=input_task2_test5, write2file=False, read_from_file=False), expectet_output_t2t5)
        self.assertEqual(solve_task2(input_file=input_task2_test6, write2file=False, read_from_file=False), expectet_output_t2t6)
        self.assertEqual(solve_task2(input_file=input_task2_test7, write2file=False, read_from_file=False), expectet_output_t2t7)


if __name__ == '__main__':
    unittest.main()