#!./venv/bin/python
import sys
import argparse
import os


def dir_path(string):
    # Set 1 when tail takes file instead of stdin
    if os.path.isdir(string):
        print(f'tail.py: {string} is a directory')
    elif os.path.isfile(string):
        return string, 1
    else:
        print(f'tail.py: {string}: No such file or directory')


def main():
    """Here we implemented tail UNIX-command. As original one it takes input from a file or from stdin.
    Output set by default to direct in stdout, you can change it by adding '> filename'  after a command.
    It can work in pipes."""
    parser = argparse.ArgumentParser('Display the last part of a file ')
    parser.add_argument('-n', help='The location is number lines', type=int)
    parser.add_argument('infile', nargs='?', type=dir_path, default=sys.stdin)
    args = parser.parse_args()
    if isinstance(args.infile, tuple):
        with open(args.infile[0]) as f:
            if args.n:
                text = f.readlines()[-args.n:]
            else:
                text = f.readlines()[-10:]
        for line in text:
            print(line, end='')
        return 0
    text = [file.strip() for file in args.infile.readlines()]
    if args.n:
        text = text[-args.n:]
    else:
        text = text[-10:]
    for line in text:
        print(line)


if __name__ == '__main__':
    main()
