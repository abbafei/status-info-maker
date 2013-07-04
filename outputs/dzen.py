#!/usr/bin/env python
import json
import util

util.outputter(lambda line: ''.join((''.join((''.join(('^fg(', d['color'], ')', d['text'].replace('^', '^^'), '^fg()')) if 'color' in d else d['text'].replace('^', '^^')) for d in json.loads(line)), '\n')))
