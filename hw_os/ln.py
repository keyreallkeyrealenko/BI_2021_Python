#!./venv/bin/python
import argparse
import os


def dir_path(string):
    if os.path.exists(string):
        return string
    else:
        print(f'ln.py {string}: No such file or directory')
        return None


def main():
    """Here we implemented mkdir UNIX-command. As original one
    it takes input as a path to new created directory."""
    parser = argparse.ArgumentParser('Creates a new directory entry (linked file) which has the same modes as the '
                                     'original fil')
    parser.add_argument('-s', help='Create a symbolic link.', action='store_true')
    parser.add_argument('infile', type=str)
    parser.add_argument('outfile', type=str, default=None, nargs='?')
    args = parser.parse_args()
    file = dir_path(args.infile)
    if not file:
        return 0
    if not args.outfile:
        print(f'{args.infile}: File exists')
        return 0
    if args.s:
        os.symlink(file, args.outfile)
        return 0
    else:
        os.link(file, args.outfile)
        return 0


if __name__ == '__main__':
    main()
