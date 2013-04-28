#!/usr/bin/env python
import json,sys
while True:
    sys.stdout.write(''.join([' | '.join(d['text'].strip() for d in json.loads(sys.stdin.readline()) if d['text'].strip() != ''), '\n']))
    sys.stdout.flush()
