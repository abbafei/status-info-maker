#!/usr/bin/env python
'''wait the specified amount of time (in seconds), default 1'''
import sys
import util

join_with = (sys.argv[1] if (len(sys.argv) > 1) else None)
util.fifo_handler(iter(sys.stdin.readline, ''), sys.stdout, after_fn=lambda i: ((join_with,) if (join_with is not None) else ()))
