#!/usr/bin/env python
import subprocess
import json,sys
default_dict_actions={
    'text': None,
    'cmd': lambda i: {'text': subprocess.Popen(i['cmd'], shell=True, stdout=subprocess.PIPE).communicate()[0]},
    'color': None,
}
dictize = lambda a: ((i if isinstance(i, dict) else {'text': i}) for i in a)
combine_dicts = lambda xs: dict((k, v) for d in xs for k, v in d.iteritems())
actize = lambda t, dict_actions=None: (combine_dicts((({n: d[n]} if a is None else a(d)) if n in d else {}) for n, a in (dict_actions if (dict_actions is not None) else default_dict_actions).iteritems()) for d in t)
denewlineize=lambda t: (dict(((k, v.rstrip('\r\n')) if k == 'text' else (k,v)) for k,v in d.iteritems()) for d in t)
def run(fpinp, fpout, dict_actions=None):
    return json.dump(list(denewlineize(actize(dictize(json.load(fpinp)), dict_actions=dict_actions))), fpout)
if __name__ == '__main__':
    run(sys.stdin, sys.stdout)
    sys.stdout.flush()
