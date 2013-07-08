#!/usr/bin/env python
import json
import util

cmder=lambda inp: json.dumps(filter(lambda a: a != {} and 'full_text' in a, (dict((('full_text', v.strip()) if k == 'text' else (k,v)) for k,v in d.iteritems() if v.strip() != '') for d in json.loads(inp))), separators=(',',':'))
util.outputter(lambda line: ''.join((',', cmder(line), '\n')), do_b4=lambda inp: (''.join(('{"version":1}\n[\n', cmder(inp.next()), '\n')),), do_after=lambda inp: (']\n',))
