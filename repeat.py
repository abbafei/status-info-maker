#!/usr/bin/env python
import time,sys,subprocess
import cStringIO as StringIO
import run
interval = float(sys.argv[1])
template = sys.stdin.read()
while True:
    run.run(StringIO.StringIO(template), sys.stdout)
    sys.stdout.write('\n')
    sys.stdout.flush()
    time.sleep(interval)
