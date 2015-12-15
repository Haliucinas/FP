#!/usr/bin/env python
import argparse
from pymonad.Maybe import *

import net

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("id")
    parser.add_argument("nums")

    [net.run * Just(id) for id in [parser.parse_args().id + str(it) for it in range(int(parser.parse_args().nums))]]