#!./venv/bin/python
import sys
import argparse
import os
import cmd


def dir_path(string):
    if os.path.isdir(string):
        return string
    elif os.path.isfile(string):
        print(string)
    else:
        print(f'{string}: No such file or directory')


def main():
    """Here we implemented ls UNIX-command. As original one it takes input as a path to a folder, by default it set
    as '.' – current folder.Output set by default to direct in stdout, you can change it by adding '> filename'
    after a command. It can work in pipes."""
    parser = argparse.ArgumentParser('list directory contents.')
    parser.add_argument('infile', nargs='?', type=dir_path, default='.')
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    parser.add_argument('-a', help='Include directory entries whose names begin with a dot', action='store_true')
    args = parser.parse_args()
    # Raise a problem if path is not valid
    if not args.infile:
        return 0
    # If '-a' argument not in a given command remove files start with '.'
    listed_dir = ['.'] + ['..'] + list(sorted(os.listdir(args.infile)))
    if not args.a:
        listed_dir = [i for i in listed_dir if not i.startswith('.')]
    cli = cmd.Cmd()
    cli.columnize(listed_dir, displaywidth=100)
    return 0


if __name__ == '__main__':
    main()
