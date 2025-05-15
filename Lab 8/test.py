import unittest

from task1 import *
from task2 import *
from task3 import *

from input_data import *

class TestStringMethods(unittest.TestCase):

    def test_task1(self):
        self.assertEqual(bwt(task1_input1, "", True), task1_output1)
        self.assertEqual(bwt(task1_input2, "", True), task1_output2)
        self.assertEqual(bwt(task1_input4, "", True), task1_output4)
        self.assertIsNotNone(bwt(task1_input3, "", True))

    def test_task2(self):
        self.assertEqual(ibwt(task2_input1, "", True), task2_output1)
        self.assertEqual(ibwt(task2_input2, "", True), task2_output2)
        self.assertEqual(ibwt(task2_input4, "", True), task2_output4)
        self.assertIsNotNone(ibwt(task2_input3, "", True))

    def test_task3(self):
        self.assertEqual(matching(task3_input1, "", True), task3_output1)
        self.assertEqual(matching(task3_input2, "", True), task3_output2)
        self.assertEqual(matching(task3_input3, "", True), task3_output3)
        self.assertEqual(matching(task3_input4, "", True), task3_output4)

if __name__ == '__main__':
    unittest.main()