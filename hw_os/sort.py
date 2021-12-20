#!./venv/bin/python
import sys
import argparse


def main():
    """Here we implemented sort UNIX-command. As original one it takes input from a file or from stdin.
    Output set by default to direct in stdout, you can change it by adding '> filename'
    after a command. It can work in pipes."""
    parser = argparse.ArgumentParser('list directory contents.')
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    args = parser.parse_args()
    text = sorted([file.strip() for file in args.infile.readlines()])
    for i in text:
        print(i)
    return 0


if __name__ == '__main__':
    main()
