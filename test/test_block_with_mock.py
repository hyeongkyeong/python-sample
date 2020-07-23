
import sys, os
import unittest, csv
from unittest.mock import Mock
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+'/src')
from block import Block
from tetris import Tetris
import constants
import pygame
class TestBlockWithMock(unittest.TestCase):
    ''' Test for Block.rodate() '''
    def test_rotate_with_mock(self):
        testsuite = []
        # Test Case
        input=0
        expected=[0,0,0,1,0,2,0,3]
        
        # Test Driver
        tetris_data=Tetris(0,0)
        self.block_data=tetris_data.block_data

        data=self.block_data[input]
        self.active_block=Block(data[0],0,0,0,data[1],data[2])
        self.active_block.get_rotated=Mock()
        self.active_block.get_rotated.side_effect=([[0,0],[6.123233995736766e-17,1.0],[1.2246467991473532e-16,2.0],[1.8369701987210297e-16,3.0]])
        self.active_block.rotate()
        actual=[]
        for shape_block in self.active_block.shape:
            actual.append(int(shape_block[0]/20))
            actual.append(int(shape_block[1]/20))
        print('actual_value:')
        print(actual)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
else:
    print('Start Test: '+__name__+'.py') 