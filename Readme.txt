B"H


A modular, flexible status line maker.

Many status line generators (e.g. i3status, conky, etc.) try to get all the info for the status-bar within one process.
This saves lots of resources. However, it also severely limits what can be included in the bar; you can only use what the author adds in.
Therefore, this utility aims to be flexible and modular, and does about *everything* with separate processes. It takes a little more computing power.
Small overhead is also an aim, however, this is only true when it does not limit flexibility much.

Summary:
	Tools to work with streams of JSON objects specifying text to show, and optionally the colors to show it in.
	The stream format is: JSON arrays, one per line. The arrays contain objects with a "text" entry and an optional "color" entry.
	The inputs can be in other formats, to be processed by 'processors', as long as there is only one item per line.
	The scripts in 'processors' take input streams and manipulate 1)the items contained therein, 2)the way the items are combined.
	The scripts in 'outputs' take a properly-formatted input stream, or a processed stream, and output the information contained therein.

Wintry:
	JSON is used to pass data around, and functionality is split up on a CPU-process level (i.e. each utility is a process).
	There are three parts, at present:
		- input: provided by the user in JSON form.
		- processors: transform input (processed or original)
		- outputs: transform input data from JSON into external formats

	All these parts either take, give, or both, one or more line(s) of arbitrary JSON arrays, one array per line. (Since newlines in JSON are encoded as "\n", any amount of JSON can be on a line).
	*These formats may change in future versions of this code.*
	Input format
		The input JSON arrays should contain zero or more strings and/or objects (maps).
		Input strings are shorthand for a map with a "text" item containing the string's value.
		Input maps have
			(1) either a "text" item, whose value is of the string type, or a "cmd" item, whose value is a shell command string
			(2) optional "color" item, which is a string containing a regular 6-hexadecimal-digit color code preceded by a "#" (e.g. #770613).
	Processor format
		Can be arbitrary values, as long as the lines they give *to an output* are in the expected format.
		(Usually it will be either in input format or in output format. "run" is the processing utility which transforms from input to output.)
	Output format
		Same as input format, however only maps are valid, and they contain only a "text" item, and optionally a "color" item too.

	Generally, the output destination determines the way the input and processors are to be used.
	These are generally 2 types of destination:
		1. takes a stream of status lines, updating its display with new lines when they are read.
		2. takes a command to run, and an amount of time to pause between each invocation of the command.
	In (1), therefore, you usually want to supply them with a stream of lines, generating new ones at an interval. The 'repeat' and 'wait' processors are very useful for this purpose.
	In (2), you usually want to supply the command to make only one line; the line is then updated when destination *reruns* the command.

This code was inspired by:
	- i3 "i3status" and "i3bar" utilities
	- Python WSGI specification

Currently licensed BSD.
