#!/usr/bin/env python
import json,sys
sys.stdout.write(''.join(['#[fg=white]|#[default]'.join(d['text'].strip() for d in json.loads(sys.stdin.readline()) if d['text'].strip() != ''), '\n']))
sys.stdout.flush()
