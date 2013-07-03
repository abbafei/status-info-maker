#!/usr/bin/env python

def fifo_handler(inp_iter, out_fd, b4_fn=lambda i, o: None, after_fn=lambda i, o: None):
    for i in inp_iter:
        b4_fn(inp_iter, out_fd)
        try:
            out_fd.write(i)
            out_fd.flush()
        except IOError as err:
            if err.errno == 32: # Unix: EPIPE Broken Pipe
                break
            else:
                raise
        after_fn(inp_iter, out_fd)
