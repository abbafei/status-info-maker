#!/usr/bin/env python
import json
import util

util.outputter(
    lambda line: util.connect_dicts(
        filter(lambda d: d['text'].strip() != '', json.loads(line)),
        quoter=lambda s: s.replace('^', '^^'),
        colorer=lambda c, s: ''.join(('^fg(', c, ')', s, '^fg()')),
        connector=' | ',
        quote_connectors=False,
    )
)
