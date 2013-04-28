run.py executes a JSON specification from STDIN and processes the things in it and puts the output to stdout. It takes no parameters.
repeat.py behaves the same as run.py, besides that it repeats what run.py does, every PARAM seconds. PARAM is giving as a command line parameter.
The scripts in 'outputs' take a stream of JSON run/repeat.py'd
(depending on the script) items from STDIN, formats them, and prints them to STDOUT. The STDOUT of these scripts can be used as input for the status bars, each using their respective Standard Input method (see http://i3wm.org/i3status/manpage.html sections 7 and 8, and http://i3wm.org/docs/userguide.html#status_command, for more info).
