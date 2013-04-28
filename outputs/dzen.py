#!/usr/bin/env python
import json,sys
while True:
    sys.stdout.write(''.join((''.join((''.join(('^fg(', d['color'], ')', d['text'].replace('^', '^^'), '^fg()')) if 'color' in d else d['text'].replace('^', '^^')) for d in json.loads(sys.stdin.readline())), '\n')))
    sys.stdout.flush()
