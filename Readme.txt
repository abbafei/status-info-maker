Tools to work with streams of JSON objects specifying text to show, and optionally the colors to show it in.
The stream format is: JSON arrays, one per line. The arrays contain objects with a "text" entry and an optional "color" entry.
The inputs can be in other formats, to be processed by 'processors', as long as there is only one item per line.
The scripts in 'processors' take input streams and manipulate 1)the items contained therein, 2)the way the items are combined.
The scripts in 'outputs' take a properly-formatted input stream, or a processed stream, and output the information contained therein.
