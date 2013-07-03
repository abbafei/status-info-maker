#!/usr/bin/env python
import json,sys
for line in iter(sys.stdin.readline, ''):
    sys.stdout.write(''.join(['#[fg=white]|#[default]'.join(d['text'].strip() for d in json.loads(line) if d['text'].strip() != ''), '\n']))
    sys.stdout.flush()
