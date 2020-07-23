
import sys, os
import unittest, csv
from unittest.mock import Mock
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+'/src')
from block import Block
from tetris import Tetris
import constants
import pygame
class TestBlock(unittest.TestCase):
    ''' Test for Block.rodate() '''
    def test_rotate_1(self):
        testsuite = []
        # Test Case (Data Set)
        with open('./test/test_block_rocate.csv') as f:
            reader = csv.reader(f)
            parameter = next(reader)
            for value in reader:
                testsuite.append({'input1':int(value[1]), 'expected':[int(value[2]), int(value[3]),int(value[4]),int(value[5]),int(value[6]),int(value[7]),int(value[8]),int(value[9])]})
        
        # Test Driver
        tetris_data=Tetris(0,0)
        self.block_data=tetris_data.block_data
        for tc in testsuite:
            data=self.block_data[tc.get('input1')]
            self.active_block=Block(data[0],0,0,0,data[1],data[2])
            self.active_block.rotate()
            actual=[]
            for shape_block in self.active_block.shape:
                actual.append(int(shape_block[0]/20))
                actual.append(int(shape_block[1]/20))
            self.assertEqual(actual, tc.get('expected'))


if __name__ == '__main__':
    unittest.main()
else:
    print('Start Test: '+__name__+'.py') 