#!/usr/bin/env python
# to be used with conky execp
import json
import util

util.outputter(lambda line: ''.join((''.join((''.join(('${color ', d['color'], '}', d['text'].replace('^', '^^'), '${color}')) if 'color' in d else d['text'].replace('$', '$$')) for d in json.loads(line)), '\n')))
