#!./venv/bin/python
import sys
import argparse
import os


def dir_path(string):
    # Set 1 when tail takes file instead of stdin
    if os.path.isdir(string):
        print(f'uniq.py: {string} is a directory')
        return None
    elif os.path.isfile(string):
        return string, 1
    else:
        print(f'uniq.py: {string}: No such file or directory')
        return None


def main():
    """Here we implemented uniq UNIX-command. As original one it takes input from a file or from stdin.
    Output set by default to direct in stdout, you can change it by adding '> filename'  after a command.
    It can work in pipes."""
    parser = argparse.ArgumentParser('Report or filter out repeated lines in a file')
    parser.add_argument('-u', help='Only output lines that are not repeated in the input.', type=str)
    parser.add_argument('infile', nargs='?', type=dir_path, default=sys.stdin)
    args = parser.parse_args()
    if not args.infile:
        return 0
    if isinstance(args.infile, tuple):
        with open(args.infile[0]) as f:
            file = f.readlines()
        if not args.u:
            cur_line = file[0].strip()
            print(cur_line)
            for line in file[1:]:
                if line.strip() != cur_line:
                    print(line, end='')
                cur_line = line.strip()
        else:
            file = set(file)
            for line in file:
                print(line, end='')
        return 0
    else:
        for line in sys.stdin:
            print(line, end='')
        return 0


if __name__ == '__main__':
    main()
