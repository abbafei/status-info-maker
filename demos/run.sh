#!/bin/sh
# uses hebcal <http://danny.sadinoff.com/hebcal/>
didir="$1"
echo "$(printf '[{"cmd": "acpi -b", "color":"#613770"}, " ", {"cmd": "hebcal -T | head -1", "color": "#0770ff"}, " ", {"cmd": "date +%%a", "color": "#07ff70"}, " ", " ", {"cmd": "date '; printf "'+%%I:%%M:%%S %%p'"; printf '","color": "#ffffff"}]'; printf '')" | 
	$didir/processors/repeat.py | $didir/processors/wait.py 1 | 
	$didir/processors/run.py | $didir/outputs/i3bar.py
