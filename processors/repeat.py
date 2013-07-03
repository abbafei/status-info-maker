#!/usr/bin/env python
'''repeat what was provided standard input the specified amount of times, or indefinitely if amount of times is not given'''
import sys
import itertools
import fifo

inp = sys.stdin.read()
times = int(sys.argv[1] if (len(sys.argv) > 1) else 0)
fifo.fifo_handler(itertools.islice(itertools.repeat(inp), (times or None)), sys.stdout)
