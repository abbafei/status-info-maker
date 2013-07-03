#!/usr/bin/env python
# to be used with conky execp
import json,sys
for line in iter(sys.stdin.readline, ''):
    sys.stdout.write(''.join((''.join((''.join(('${color ', d['color'], '}', d['text'].replace('^', '^^'), '${color}')) if 'color' in d else d['text'].replace('$', '$$')) for d in json.loads(line)), '\n')))
    sys.stdout.flush()
