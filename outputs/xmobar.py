#!/usr/bin/env python
import json
import util

util.outputter(lambda line: ''.join(('}{', ''.join((''.join(('<fc=', d['color'], '>', d['text'], '</fc>')) if 'color' in d else d['text']) for d in json.loads(line)), '\n')))
