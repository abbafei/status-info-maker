#!/usr/bin/env python
import json,sys
cmder=lambda: json.dumps(filter(lambda a: a != {} and 'full_text' in a, (dict((('full_text', v.strip()) if k == 'text' else (k,v)) for k,v in d.iteritems() if v.strip() != '') for d in json.loads(sys.stdin.readline()))), separators=(',',':'))
sys.stdout.write('{"version":1}\n[\n')
sys.stdout.write(''.join((cmder(), '\n')))
sys.stdout.flush()
while True:
    sys.stdout.write(''.join((',', cmder(), '\n')))
    sys.stdout.flush()
