#!/usr/bin/env python
# can be used with, among many options, with XMLHTTPRequest multipart push
import json
import cgi
import util

util.outputter(
    lambda line: util.connect_dicts(
        filter(lambda d: d['text'].strip() != '', json.loads(line)),
        quoter=lambda s: cgi.escape(s),
        colorer=lambda c, s: ''.join(('<span style="color: ', c, '">', s, '</span>')),
        connector=' <span style="font-weight: bold">|</span> ',
        quote_connectors=False,
    )
)
