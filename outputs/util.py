#!/usr/bin/env python
import sys

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
