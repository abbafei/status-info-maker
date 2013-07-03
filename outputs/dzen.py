#!/usr/bin/env python
import json,sys
for line in iter(sys.stdin.readline, ''):
    sys.stdout.write(''.join((''.join((''.join(('^fg(', d['color'], ')', d['text'].replace('^', '^^'), '^fg()')) if 'color' in d else d['text'].replace('^', '^^')) for d in json.loads(line)), '\n')))
    sys.stdout.flush()
