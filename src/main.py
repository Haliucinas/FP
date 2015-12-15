#!/usr/bin/env python
import argparse
from pymonad.Maybe import *
from pymonad.List import *
from multiprocessing import Process

import net

def worker(_id, nums, req, player):
    [net.run * Just((id, player, req)) for id in [_id + str(it) for it in range(nums)]]

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('id1')
    parser.add_argument('id2')
    parser.add_argument('nums')

    processes = [
        Process(target=worker, args=(parser.parse_args().id1, int(parser.parse_args().nums), net.post, 1,)),
        Process(target=worker, args=(parser.parse_args().id2, int(parser.parse_args().nums), net.get, 2,))
    ]

    [process.start() for process in processes]