# mdc

A simple tool to convert regular code to Markdown code blocks.

## Usage

Running `mdc` from the command line without any arguments will take the contents of your clipboard, adds tabs in front of it and places it on the clipboard again:

	$ # Clipboard: 'test'
	$ mdc
	$ # Clipboard: '	test'

Optional arguments:

	-f, --file
		Load code from file
	-s, --spaces
		Place spaces in front of code instead of tabs
