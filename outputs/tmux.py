#!/usr/bin/env python
# For use with options status-left, status-right, and similar options, by wrapping the command to display a line in "#(<commands to sh>)" (including the quotes). *-bg options can be used to change the background colors; *-interval changes how often it is refreshed (so also reran); *-length changes how large the display area is. (color rgb codes are supported from version 1.5 (released in 2011) onwards.)
import json
import util

util.outputter(lambda line: ''.join(['#[fg=white]|#[default]'.join(''.join(('#[fg=', d['color'], ']',  d['text'].strip(), '#[default]')) for d in json.loads(line) if d['text'].strip() != ''), '\n']))
