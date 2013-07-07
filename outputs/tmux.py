#!/usr/bin/env python
# For use with options status-left, status-right, and similar options, by wrapping the command to display a line in "#(<commands to sh>)" (including the quotes). *-bg options can be used to change the background colors; *-interval changes how often it is refreshed (so also reran); *-length changes how large the display area is. (color rgb codes are supported from version 1.5 (released in 2011) onwards.)
import json
import util

util.outputter(
    lambda line: util.connect_dicts(
        filter(lambda d: d['text'].strip() != '', json.loads(line)),
        quoter=lambda s: s.replace('#', '##'),
        colorer=lambda c, s: ''.join(('[#fg=', c, ']', s, '#[fg=default]')),
        connector='#[fg=white]|#[fg=default]',
        quote_connectors=False,
    )
)
