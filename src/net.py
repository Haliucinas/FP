#!/usr/bin/env python
import requests
from pymonad.Maybe import *

import utils

def run(id):

	def runImpl(idx):
		post(id, 1, 'scala+list', utils.predefinedMove('scala+list', idx).value)
		get(id, 2, 'json+list')

		if idx == 8: return Nothing
		
		post(id, 2, 'm-expr+list', utils.predefinedMove('m-expr+list', idx+1).value)
		get(id, 1, 'bencode+list')
		runImpl * Just(idx+2)

	runImpl * Just(0)


def makeUrl(id, player):
    return "http://tictactoe.homedir.eu/game/" + id + "/player/" + str(player)

def post(id, player, protocol, payload):
    r = requests.post(makeUrl(id, player), headers = {'Content-Type': 'application/'+ protocol}, data = payload)
    print('<< |', id, player, protocol)

def get(id, player, protocol):
    r = requests.get(makeUrl(id, player), headers = {'Accept': 'application/'+ protocol})
    print('>> |', id, player, protocol)