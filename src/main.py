#!/usr/bin/env python
import argparse
from pymonad.Maybe import *
from pymonad.List import *
from multiprocessing import Process

import net

def worker(_id, nums, req, player, protocol):
    [net.run * Just((id, player, req, protocol)) for id in [_id + str(it) for it in range(nums)]]

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('id1')
    parser.add_argument('id2')
    parser.add_argument('nums')

    processes = [
        Process(target=worker, args=(parser.parse_args().id1, int(parser.parse_args().nums), net.post, 1, 'scala+list',)),
        Process(target=worker, args=(parser.parse_args().id2, int(parser.parse_args().nums), net.get, 2, 'json+list',))
    ]

    [process.start() for process in processes]