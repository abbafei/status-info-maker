#!/usr/bin/env python
'''wait the specified amount of time (in seconds), default 1'''
import time
import sys
import util

interval = float(sys.argv[1] if (len(sys.argv) > 1) else 1)
util.fifo_handler(iter(sys.stdin.readline, ''), sys.stdout, after_fn=lambda i: ((interval > 0) and time.sleep(interval),())[1])
