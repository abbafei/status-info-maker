#!/usr/bin/env python
import sys
import json




def connect_dicts(item, connector=' | ', quoter=lambda text: text, colorer=lambda color, text: text, quote_connectors=True):
    _format_t = lambda t: (lambda pqt: (colorer(t['color'], pqt) if ('color' in t) else pqt))(quoter(t['text']))
    dicts = (_format_t(t) for t in item)
    si = (quoter(connector) if quote_connectors else connector).join(dicts)
    return ''.join((si, "\n"))


def process_dicts(dicts, fn):
    return (dict((k, fn(k, v)) for k, v in d) for d in dicts)
    


def outputter(outp_gen=lambda item: item, inp_iter=iter(sys.stdin.readline, ''), outp_fd=sys.stdout, do_b4=lambda inp, outp_fn: None, do_after=lambda outp_fn: None):
    def _writer_fd(fd):
        def _writer(s):
            fd.write(s)
            fd.flush()
        return _writer
    w = _writer_fd(outp_fd)
    b4 = do_b4(inp_iter, w)
    if b4 is not None:
        w(b4)
    for item in inp_iter:
        outp_fd.write(outp_gen(item))
        outp_fd.flush()
    after = do_after(w)
    if after is not None:
        w(after)
