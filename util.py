#!/usr/bin/env python
import sys
import json
import itertools




def connect_dicts(item, connector=' | ', quoter=lambda text: text, colorer=lambda color, text: text, quote_connectors=True):
    _format_t = lambda t: (lambda pqt: (colorer(t['color'], pqt) if ('color' in t) else pqt))(quoter(t['text']))
    dicts = (_format_t(t) for t in item)
    si = (quoter(connector) if quote_connectors else connector).join(dicts)
    return ''.join((si, "\n"))


def writer_fd(fd):
    def _writer(data):
        fd.write(data)
        fd.flush()
    return _writer


def loopy(inp=iter(sys.stdin.readline, ''), outp=writer_fd(sys.stdout), each_fn=None, b4_fn=None, after_fn=None):
    do_b4 = ((lambda i: ()) if (b4_fn is None) else b4_fn)
    do_each = ((lambda item: ()) if (each_fn is None) else each_fn)
    do_after = ((lambda i: ()) if (after_fn is None) else after_fn)
    for o in itertools.chain(do_b4(inp), itertools.chain.from_iterable(do_each(item) for item in inp), do_after(inp)):
        outp(o)


def outputter(outp_gen=lambda item: item, inp_iter=iter(sys.stdin.readline, ''), outp_fd=sys.stdout, do_b4=None, do_after=None):
    w = writer_fd(outp_fd)
    return loopy(
        inp_iter,
        w,
        b4_fn=do_b4,
        after_fn=do_after,
        each_fn=lambda item: (outp_gen(item),),
    )


def fifo_handler(inp, outp, b4_fn=lambda i: (), after_fn=lambda i: ()):
    write = writer_fd(outp)
    for item in inp:
        for i in b4_fn(item):
            write(i)
        try:
            write(item)
        except IOError as err:
            if err.errno == 32: # Unix: EPIPE Broken Pipe
                break
            else:
                raise
        for i in after_fn(item):
            write(i)
