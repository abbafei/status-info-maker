#!/usr/bin/env sh
# uses hebcal <http://danny.sadinoff.com/hebcal/>
D="$(dirname "$(dirname "$(readlink -f "$(dirname "$(which "$0" || echo "$0")")")")")"
didir="$D"

printf 'Content-Type: text/html\r\n\r\n'
printf '<html><head><meta http-equiv="refresh" content="1; url="'
echo "$REQUEST_URI" | head -c -1
printf '"><title>Jewcal</title></head><body style="background: black; color: white"><p>'
echo "$(printf '[{"cmd": "hebcal -T | head -1", "color": "#0770ff"}, " ", {"cmd": "date +%%a", "color": "#07ff70"}, " ", {"cmd": "date '; printf "'+%%I:%%M:%%S %%p'"; printf '","color": "#ffffff"}]'; printf '')" | $didir/processors/run.py | $didir/outputs/html.py | head -c -1
printf '</p</body></html>'
