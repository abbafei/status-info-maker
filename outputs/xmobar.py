#!/usr/bin/env python
import json,sys
while True:
    sys.stdout.write(''.join(('}{', ''.join((''.join(('<fc=', d['color'], '>', d['text'], '</fc>')) if 'color' in d else d['text']) for d in json.loads(sys.stdin.readline())), '\n')))
    sys.stdout.flush()
