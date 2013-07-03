#!/usr/bin/env python
'''runs the cmds in the json objects and outputs them as texts'''
import subprocess
import json
import sys

default_dict_actions={
    'text': None,
    'cmd': lambda i: {'text': subprocess.Popen(i['cmd'], shell=True, stdout=subprocess.PIPE).communicate()[0]},
    'color': None,
}
dictize = lambda a: ((i if isinstance(i, dict) else {'text': i}) for i in a)
combine_dicts = lambda xs: dict((k, v) for d in xs for k, v in d.iteritems())
actize = lambda t, dict_actions=None: (combine_dicts((({n: d[n]} if a is None else a(d)) if n in d else {}) for n, a in (dict_actions if (dict_actions is not None) else default_dict_actions).iteritems()) for d in t)
denewlineize=lambda t: (dict(((k, v.rstrip('\r\n')) if k == 'text' else (k,v)) for k,v in d.iteritems()) for d in t)
jsonloadize=lambda inp_fd: (json.loads(i) for i in iter(inp_fd.readline, ''))
jsondumpize=lambda ts: (''.join((json.dumps(tuple(t)), "\n")) for t in ts)
if __name__ == '__main__':
    import fifo

    fifo.fifo_handler(jsondumpize(denewlineize(actize(dictize(i))) for i in jsonloadize(sys.stdin)), sys.stdout)
