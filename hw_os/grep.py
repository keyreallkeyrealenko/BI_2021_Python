#!./venv/bin/python
"""To now it doesn't work with regular expressions. I'll fix it later."""
import os
import argparse
import re
import sys


def dir_path(string):
    # Set 1 when grep takes file instead of stdin
    if os.path.isdir(string):
        print(f'grep.py: {string} is a directory')
    elif os.path.isfile(string):
        return string, 1
    else:
        print(f'grep.py: {string}: No such file or directory')


def main():
    """Here we implemented grep UNIX-command. As original one it takes input as a pattern and a path to a file,
    by default it takes pattern from stdin. Output set by default in stdout, you can change it by adding '> filename'
    after a command. It can work in pipes."""
    parser = argparse.ArgumentParser('It searches any given input files')
    parser.add_argument('pattern', type=str)
    parser.add_argument('infile', nargs='?', type=dir_path, default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    args = parser.parse_args()
    pattern = re.compile(args.pattern)
    if not args.infile:
        return 0
    # Handle the case when input is a text file
    if isinstance(args.infile, tuple):
        with open(args.infile[0]) as f:
            text = f.readlines()
        for line in text:
            line = line.strip()
            ans = line
            for m in pattern.finditer(line):
                ans = ans[:m.start()] + m.group().upper() + ans[m.end():]
            if ans != line:
                print(ans)
        return 0
    # Handle the case when input is stdin
    for line in sys.stdin:
        ans = line
        for m in pattern.finditer(line):
            ans = ans[:m.start()] + m.group().upper() + ans[m.end():]
        if ans != line:
            print(ans, end='')
    return 0


if __name__ == '__main__':
    main()
