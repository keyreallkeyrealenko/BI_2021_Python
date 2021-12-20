#!./venv/bin/python
import argparse
import shutil
import os


def dir_path(string):
    if os.path.exists(string):
        return string
    else:
        print(f'cp.py {string}: No such file or directory')
        return None


def main():
    """Here we implemented cp UNIX-command. As original one it takes input as a file or a folder,
    output as a path where to save a file or a folder."""
    parser = argparse.ArgumentParser('It copies the contents of the source_file to the target_file')
    parser.add_argument('-r', help='cp.py copies the directory and the entire subtree connected at'
                                   ' that point.', action='store_true')
    parser.add_argument('infile', type=str)
    parser.add_argument('outfile', type=str, default=None, nargs='?')
    args = parser.parse_args()
    file = dir_path(args.infile)
    if not file:
        return 0
    if not args.outfile:
        print('usage: cp [-r] source_file target_file')
    if os.path.isdir(args.infile) and not args.r:
        print(f'cp: {args.infile} is a directory (not copied).')
        return 0
    elif os.path.isdir(file) and args.r:
        shutil.copytree(file, args.outfile)
        return 0
    elif os.path.isfile(file) and not args.r:
        shutil.copy(file, args.outfile)
        return 0


if __name__ == '__main__':
    main()
