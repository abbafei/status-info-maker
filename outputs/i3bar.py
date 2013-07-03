#!/usr/bin/env python
import json,sys
cmder=lambda inp: json.dumps(filter(lambda a: a != {} and 'full_text' in a, (dict((('full_text', v.strip()) if k == 'text' else (k,v)) for k,v in d.iteritems() if v.strip() != '') for d in json.loads(inp))), separators=(',',':'))
sys.stdout.write('{"version":1}\n[\n')
sys.stdout.write(''.join((cmder(sys.stdin.readline()), '\n')))
sys.stdout.flush()
for line in iter(sys.stdin.readline, ''):
    sys.stdout.write(''.join((',', cmder(line), '\n')))
    sys.stdout.flush()
sys.stdout.write(']\n')
