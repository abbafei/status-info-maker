#!/usr/bin/env python
import json
import util

util.outputter(
    lambda line: util.connect_dicts(
        filter(lambda d: d['text'].strip() != '', json.loads(line)),
    )
)
