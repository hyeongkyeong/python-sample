
import sys, os
import unittest, csv
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+'/src')
from calculator import absolute
from unittest.mock import MagicMock

class TestCalculator(unittest.TestCase):
    ''' Tests for Calculator() '''

    def test_absolute_1(self):
        # Test Case
        input = -100
        expected = 100
        # Test Driver
        actual = absolute(input)
        self.assertEqual(actual, expected)

    def test_absolute_2(self):
        # Test Case
        input = 100
        expected = -100
        # Test Driver
        actual = absolute(input)
        self.assertEqual(actual, expected)

    def test_absolute_3(self):
        # Test Case
        input = -9999999
        expected = 9999999
        # Test Driver
        actual = absolute(input)
        self.assertEqual(actual, expected)

    def test_absolute_4(self):
        # Test Case
        input = 0
        expected = 0
        # Test Driver
        actual = absolute(input)
        self.assertEqual(actual, expected)

    def test_absolute_5(self):
        testsuite = []
        # Test Case (Data Set)
        with open('./test/test_calculator_absolute.csv') as f:
            reader = csv.reader(f)
            parameter = next(reader)
            for value in reader:
                testsuite.append({'input1':int(value[0]), 'expected':int(value[1])})
        # Test Driver
        for tc in testsuite:
            actual = absolute(tc.get('input1'))
            self.assertEqual(actual, tc.get('expected'))


if __name__ == '__main__':
    reportFoler = "UnitTest"
    unittest.main()
else:
    print('Start Test: '+__name__+'.py') 