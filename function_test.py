
import sys, os
import xmlrunner
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+'/src')
from tetris import Tetris

# def runner(output='./test/output'):
#     return xmlrunner.XMLTestRunner(output=output)

# def find_tests():
#     return unittest.TestLoader().discover('test')

if __name__ == '__main__':
    Tetris(16,30).run()