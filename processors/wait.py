#!/usr/bin/env python
'''wait the specified amount of time (in seconds), default 1'''
import time
import sys
import fifo

interval = float(sys.argv[1] if (len(sys.argv) > 1) else 1)
fifo.fifo_handler(iter(sys.stdin.readline, ''), sys.stdout, after_fn=lambda i, o: ((interval > 0) and time.sleep(interval)))
