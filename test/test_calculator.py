
import sys, os
import unittest, csv
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+'/src')
from calculator import absolute


class TestSample(unittest.TestCase):
    ''' Tests for Calculator() '''
    def test_absolute(self):
        testsuite = []

        with open('./test/test_calculator_absolute.csv') as f:
            reader = csv.reader(f)
            for value in reader:
                testsuite.append({'input1':int(value[0]), 'expected':int(value[1])})

        for tc in testsuite:
            actual = absolute(tc.get('input1'))
            self.assertEqual(actual, tc.get('expected'))


if __name__ == '__main__':
    unittest.main()
else:
    print('Start Test: '+__name__+'.py') 