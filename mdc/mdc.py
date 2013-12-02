#!/usr/bin/env python

import xerox
import argparse

def parse_args():
  parser = argparse.ArgumentParser()

  parser.add_argument('-s', '--spaces', help='Use spaces', action='store_true')
  parser.add_argument('-f', '--file', help='Load code from file')
  # parser.add_argument('-o', '--out', help='File to place output code')

  return parser.parse_args()

def get_code(args):
  code = ''

  if args.file is not None and type(args.file) is str:
    f = open(args.file)
    code = f.read()
  else:
    code = xerox.paste()

  return code

def add_indentation(code, tab=True, spaces=4, tabs=1):
  md = ''
  indentation = ''
  count = tabs if tab else spaces
  t = '\t' if tab else ' '

  for i in range(0, count): indentation += t
  for line in code.split('\n'): md += indentation + line + '\n'

  return md

def main():
  args = parse_args()

  tab = not args.spaces
  code = add_indentation(get_code(args), tab)
  xerox.copy(code)

if __name__ == "__main__":
  main()
