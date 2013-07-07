#!/usr/bin/env python
# to be used with conky execp, for example: conky -t '${execp <command>}'
import json
import util

util.outputter(
    lambda line: util.connect_dicts(
        filter(lambda d: d['text'].strip() != '', json.loads(line)),
        quoter=lambda s: s.replace('$', '$$'),
        colorer=lambda c, s: ''.join(('${color ', c, '}', s, '${color}')),
        connector=' | ',
        quote_connectors=False,
    )
)
