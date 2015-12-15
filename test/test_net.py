#!/usr/bin/env python

import sys
sys.path.append('../src/')
import unittest

import net

class TestNet(unittest.TestCase):
	
	def test_url_generation(self):
		url = net.makeUrl('abc', 1)
		self.assertEqual(url, 'http://tictactoe.homedir.eu/game/abc/player/1')
		self.assertNotEqual(url, 'http://tictactoe.homedir.eu/game/abc/player/2')

if __name__ == '__main__':
    unittest.main()