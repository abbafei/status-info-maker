#!/usr/bin/env python
import json
import util

util.outputter(lambda line: ''.join([' | '.join(d['text'].strip() for d in json.loads(line) if d['text'].strip() != ''), '\n']))
