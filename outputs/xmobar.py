#!/usr/bin/env python
import json,sys
for line in iter(sys.stdin.readline, ''):
    sys.stdout.write(''.join(('}{', ''.join((''.join(('<fc=', d['color'], '>', d['text'], '</fc>')) if 'color' in d else d['text']) for d in json.loads(line)), '\n')))
    sys.stdout.flush()
