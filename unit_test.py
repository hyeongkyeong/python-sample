import unittest
import HtmlTestRunner
import xmlrunner


def runner(output='./test/report'):
    return HtmlTestRunner.HTMLTestRunner(output=output)
    # return xmlrunner.XMLTestRunner(output=output)

def find_tests():
    return unittest.TestLoader().discover('test')

if __name__ == '__main__':
    runner().run(find_tests())