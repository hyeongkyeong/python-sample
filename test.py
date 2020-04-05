import unittest
import xmlrunner

def runner(output='./test/output'):
    return xmlrunner.XMLTestRunner(output=output)

def find_tests():
    return unittest.TestLoader().discover('test')

if __name__ == '__main__':
    print('start test!')
    runner().run(find_tests())