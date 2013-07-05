#!/usr/bin/env python
#formats items as array of dicts
import sys
import fifo
import run
dict_actions={
    'text': None,
    'cmd': None,
    'color': None,
}


fifo.fifo_handler(run.jsondumpize(run.denewlineize(run.actize(run.dictize(i), dict_actions=dict_actions)) for i in run.jsonloadize(sys.stdin)), sys.stdout)
