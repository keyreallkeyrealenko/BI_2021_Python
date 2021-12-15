#!./venv/bin/python
import sys
import argparse
import os


def dir_path(string):
    # Set 1 when cat takes file instead of stdin
    if os.path.isdir(string):
        print(f'cat.py: {string} is a directory')
    elif os.path.isfile(string):
        return string, 1
    else:
        print(f'cat.py: {string}: No such file or directory')


def main():
    """Here we implemented cat UNIX-command. As original one it takes input from a file or from stdin.
    Output set by default to direct in stdout, you can change it by adding '> filename'  after a command.
    It can work in pipes."""
    parser = argparse.ArgumentParser('Count lines, words or bytes. ')
    parser.add_argument('infile', nargs='?', type=dir_path, default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    args = parser.parse_args()
    if isinstance(args.infile, tuple):
        with open(args.infile[0]) as f:
            for line in f.readlines():
                print(line, end='')
        return 0
    for line in sys.stdin:
        print(line, end='')


if __name__ == '__main__':
    main()
