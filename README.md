# mdc

A simple tool to convert regular code to Markdown code blocks.

## Usage

Running `mdc` from the command line without any arguments will take the contents of your clipboard, adds tabs in front of it and places it on the clipboard again:

	$ # Clipboard: 'test'
	$ mdc
	$ # Clipboard: '	test'

Full usage:

	usage: mdc [options]

	optional arguments:
	  -h, --help            show this help message and exit
	  -s, --spaces          use spaces instead of tabs
	  -f FILE, --file FILE  load from file
	  -o, --stdout          print parsed code to stdout
