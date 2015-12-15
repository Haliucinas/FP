#!/usr/bin/env python

import sys
sys.path.append('../src/')
import unittest
import string
from pymonad.Maybe import *

import utils

class TestUtils(unittest.TestCase):
	
	def test_random_char_gen(self):
		str1 = utils.random_char(16)
		self.assertEqual(len(str1), 16)
		self.assertNotEqual(str1, '')
		self.assertTrue(str1.isalpha())

		str2 = utils.random_char(16)
		self.assertNotEqual(str1, str2)
		self.assertEqual(len(str1), len(str2))

	def test_predefined_moves(self):
		move = utils.predefinedMove('scala+list', 0)
		self.assertEqual(move, Just('List(Map(x -> 1, y -> 2, v -> x))'))
		self.assertEqual(utils.predefinedMove('not-existing-key', 0), Nothing)


if __name__ == '__main__':
    unittest.main()